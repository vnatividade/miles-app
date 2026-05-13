from datetime import date

import pytest
from pydantic import ValidationError

from miles_app.scrapers import (
    BaseScraper,
    NormalizedScraperResult,
    RawScraperResult,
    ScraperExecutionConfig,
    ScraperExecutionFailed,
    ScraperProviderError,
    ScraperSearchCriteria,
    ScraperSearchResult,
)


class SuccessfulFakeScraper(BaseScraper):
    provider = "fake"

    def _search_once(
        self,
        criteria: ScraperSearchCriteria,
        config: ScraperExecutionConfig,
    ) -> ScraperSearchResult:
        raw = RawScraperResult(
            provider=self.provider,
            search_input=criteria.model_dump(mode="json"),
            raw_payload={"miles": 55000},
            source_url="https://example.com/results",
        )
        normalized = NormalizedScraperResult(
            provider=self.provider,
            airline="Example Air",
            origin=criteria.origin_airport,
            destination=criteria.destination_airport,
            departure_date=criteria.start_date,
            return_date=criteria.end_date,
            miles_price=55000,
            cash_fee=250.00,
            currency="BRL",
            cabin_class=criteria.cabin_class,
            stops=0,
            flight_duration="8h 35m",
            availability="available",
            source_url="https://example.com/results",
        )
        return ScraperSearchResult(
            provider=self.provider,
            criteria=criteria,
            raw_results=[raw],
            normalized_results=[normalized],
        )


class FlakyFakeScraper(SuccessfulFakeScraper):
    def __init__(self, config: ScraperExecutionConfig | None = None) -> None:
        super().__init__(config)
        self.attempts = 0
        self.sleep_calls: list[float] = []

    def _search_once(
        self,
        criteria: ScraperSearchCriteria,
        config: ScraperExecutionConfig,
    ) -> ScraperSearchResult:
        self.attempts += 1
        if self.attempts == 1:
            raise ScraperProviderError("temporary provider failure", retryable=True)
        return super()._search_once(criteria, config)

    def _sleep_before_retry(self, seconds: float) -> None:
        self.sleep_calls.append(seconds)


class NonRetryableFakeScraper(FlakyFakeScraper):
    def _search_once(
        self,
        criteria: ScraperSearchCriteria,
        config: ScraperExecutionConfig,
    ) -> ScraperSearchResult:
        self.attempts += 1
        raise ScraperProviderError("captcha required", retryable=False)


def _criteria() -> ScraperSearchCriteria:
    return ScraperSearchCriteria(
        origin_airport="gru",
        destination_airport="mia",
        start_date=date(2026, 6, 1),
        end_date=date(2026, 6, 15),
        cabin_class="economy",
        passengers=2,
    )


def test_scraper_search_contract_returns_raw_and_normalized_results() -> None:
    # Arrange
    scraper = SuccessfulFakeScraper()

    # Act
    result = scraper.search(_criteria())

    # Assert
    assert result.provider == "fake"
    assert result.criteria.origin_airport == "GRU"
    assert result.raw_results[0].raw_payload == {"miles": 55000}
    assert result.normalized_results[0].origin == "GRU"
    assert result.normalized_results[0].destination == "MIA"


def test_scraper_retries_retryable_provider_errors() -> None:
    # Arrange
    config = ScraperExecutionConfig(retry_limit=2, retry_backoff_seconds=0.25)
    scraper = FlakyFakeScraper(config)

    # Act
    result = scraper.search(_criteria())

    # Assert
    assert result.provider == "fake"
    assert scraper.attempts == 2
    assert scraper.sleep_calls == [0.25]


def test_scraper_does_not_retry_non_retryable_errors() -> None:
    # Arrange
    scraper = NonRetryableFakeScraper(ScraperExecutionConfig(retry_limit=2))

    # Act / Assert
    with pytest.raises(ScraperExecutionFailed) as exc_info:
        scraper.search(_criteria())

    assert scraper.attempts == 1
    assert exc_info.value.provider == "fake"
    assert exc_info.value.attempts == 1


def test_scraper_search_criteria_rejects_invalid_date_range() -> None:
    # Arrange / Act / Assert
    with pytest.raises(ValidationError):
        ScraperSearchCriteria(
            origin_airport="GRU",
            destination_airport="MIA",
            start_date=date(2026, 6, 15),
            end_date=date(2026, 6, 1),
        )
