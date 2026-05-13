import logging
from abc import ABC, abstractmethod
from datetime import UTC, date, datetime
from time import sleep
from typing import Any, ClassVar, Literal

from pydantic import BaseModel, Field, field_validator, model_validator

CabinClass = Literal["economy", "premium_economy", "business", "first"]

logger = logging.getLogger(__name__)


class ScraperExecutionConfig(BaseModel):
    timeout_seconds: int = Field(
        default=30,
        ge=1,
        le=300,
        description="Provider request timeout budget in seconds.",
    )
    retry_limit: int = Field(
        default=3,
        ge=0,
        le=5,
        description="Number of retry attempts after the first provider failure.",
    )
    retry_backoff_seconds: float = Field(
        default=1.0,
        ge=0,
        le=60,
        description="Fixed delay between retry attempts.",
    )


class ScraperSearchCriteria(BaseModel):
    origin_airport: str = Field(
        min_length=3,
        max_length=3,
        description="IATA origin airport code.",
        examples=["GRU"],
    )
    destination_airport: str = Field(
        min_length=3,
        max_length=3,
        description="IATA destination airport code.",
        examples=["MIA"],
    )
    start_date: date = Field(description="First departure date to search.")
    end_date: date = Field(description="Last departure date to search.")
    flexibility_days: int = Field(
        default=0,
        ge=0,
        le=30,
        description="Date flexibility that provider implementations may use when supported.",
    )
    cabin_class: CabinClass = Field(default="economy", description="Requested cabin class.")
    passengers: int = Field(
        default=1,
        ge=1,
        le=9,
        description="Number of passengers to search for.",
    )
    nonstop_only: bool = Field(
        default=False,
        description="Whether provider search should request nonstop results when supported.",
    )

    @field_validator("origin_airport", "destination_airport", mode="before")
    @classmethod
    def normalize_airport_code(cls, value: str) -> str:
        if not isinstance(value, str):
            return value
        return value.strip().upper()

    @model_validator(mode="after")
    def validate_date_range(self) -> "ScraperSearchCriteria":
        if self.end_date < self.start_date:
            raise ValueError("end_date must be on or after start_date.")
        return self


class RawScraperResult(BaseModel):
    provider: str = Field(
        description="Provider that produced the raw payload.",
        examples=["smiles"],
    )
    search_input: dict[str, Any] = Field(description="Input used for the provider search.")
    raw_payload: Any = Field(description="Unmodified provider payload or extracted raw record.")
    source_url: str | None = Field(
        default=None,
        description="Provider URL related to the raw result, when available.",
    )
    captured_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
        description="Timestamp when the payload was captured.",
    )


class NormalizedScraperResult(BaseModel):
    provider: str = Field(description="Provider that produced the result.", examples=["smiles"])
    airline: str | None = Field(default=None, description="Operating or marketing airline.")
    origin: str = Field(min_length=3, max_length=3, description="IATA origin airport code.")
    destination: str = Field(
        min_length=3,
        max_length=3,
        description="IATA destination airport code.",
    )
    departure_date: date = Field(description="Outbound departure date.")
    return_date: date | None = Field(default=None, description="Optional return date.")
    miles_price: int | None = Field(
        default=None,
        ge=0,
        description="Mileage price, when available.",
    )
    cash_fee: float | None = Field(default=None, ge=0, description="Cash fee, when available.")
    currency: str | None = Field(
        default=None,
        min_length=3,
        max_length=3,
        description="ISO currency code for cash fees.",
    )
    cabin_class: CabinClass = Field(description="Cabin class.")
    stops: int | None = Field(default=None, ge=0, description="Number of stops, when available.")
    flight_duration: str | None = Field(default=None, description="Human-readable flight duration.")
    availability: str = Field(description="Provider availability status.")
    source_url: str | None = Field(default=None, description="Provider URL for result review.")
    captured_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
        description="Timestamp when the result was captured.",
    )

    @field_validator("origin", "destination", mode="before")
    @classmethod
    def normalize_airport_code(cls, value: str) -> str:
        if not isinstance(value, str):
            return value
        return value.strip().upper()


class ScraperSearchResult(BaseModel):
    provider: str = Field(description="Provider that executed the search.", examples=["smiles"])
    criteria: ScraperSearchCriteria = Field(description="Search criteria used by the provider.")
    raw_results: list[RawScraperResult] = Field(
        default_factory=list,
        description="Raw provider records captured during the search.",
    )
    normalized_results: list[NormalizedScraperResult] = Field(
        default_factory=list,
        description="Normalized intermediate results for persistence and matching.",
    )


class ScraperProviderError(Exception):
    def __init__(self, message: str, *, retryable: bool = True) -> None:
        super().__init__(message)
        self.retryable = retryable


class ScraperExecutionFailed(Exception):
    def __init__(self, provider: str, attempts: int, cause: ScraperProviderError) -> None:
        super().__init__(f"{provider} scraper failed after {attempts} attempt(s): {cause}")
        self.provider = provider
        self.attempts = attempts
        self.cause = cause


class BaseScraper(ABC):
    provider: ClassVar[str]

    def __init__(self, config: ScraperExecutionConfig | None = None) -> None:
        self.config = config or ScraperExecutionConfig()

    def search(self, criteria: ScraperSearchCriteria) -> ScraperSearchResult:
        attempts = self.config.retry_limit + 1
        last_error: ScraperProviderError | None = None

        for attempt in range(1, attempts + 1):
            try:
                return self._search_once(criteria, self.config)
            except ScraperProviderError as exc:
                last_error = exc
                if not exc.retryable or attempt == attempts:
                    raise ScraperExecutionFailed(self.provider, attempt, exc) from exc

                logger.warning(
                    "Retrying %s scraper after retryable error on attempt %s/%s: %s",
                    self.provider,
                    attempt,
                    attempts,
                    exc,
                )
                self._sleep_before_retry(self.config.retry_backoff_seconds)

        raise ScraperExecutionFailed(self.provider, attempts, last_error)

    @abstractmethod
    def _search_once(
        self,
        criteria: ScraperSearchCriteria,
        config: ScraperExecutionConfig,
    ) -> ScraperSearchResult:
        """Execute one provider search attempt using the provided timeout/retry config."""

    def _sleep_before_retry(self, seconds: float) -> None:
        sleep(seconds)
