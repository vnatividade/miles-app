from typing import Annotated, Any

from fastapi import APIRouter, Depends, HTTPException, Query, Response, status

from miles_app.api.dependencies import get_alert_service
from miles_app.schemas.alerts import AlertCreateRequest, AlertResponse, AlertUpdateRequest
from miles_app.services import AlertNotFoundError, AlertService, AlertValidationError

AlertServiceDependency = Annotated[AlertService, Depends(get_alert_service)]

router = APIRouter(prefix="/alerts", tags=["alerts"])


def _validation_error_response(exc: AlertValidationError) -> HTTPException:
    return HTTPException(status_code=422, detail=str(exc))


def _not_found_response(exc: AlertNotFoundError) -> HTTPException:
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc))


@router.post(
    "",
    response_model=AlertResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create alert",
    description="Create a mileage flight monitoring alert configuration.",
    responses={
        status.HTTP_201_CREATED: {"description": "Alert created."},
        422: {"description": "Invalid alert payload."},
    },
)
def create_alert(
    payload: AlertCreateRequest,
    service: AlertServiceDependency,
) -> AlertResponse:
    try:
        alert = service.create_alert(payload.model_dump())
    except AlertValidationError as exc:
        raise _validation_error_response(exc) from exc
    return AlertResponse.model_validate(alert)


@router.get(
    "",
    response_model=list[AlertResponse],
    summary="List alerts",
    description="List alert configurations, optionally filtered by user identifier.",
    responses={status.HTTP_200_OK: {"description": "Alerts returned."}},
)
def list_alerts(
    service: AlertServiceDependency,
    user_id: Annotated[int | None, Query(gt=0, description="Optional user filter.")] = None,
) -> list[AlertResponse]:
    return [AlertResponse.model_validate(alert) for alert in service.list_alerts(user_id=user_id)]


@router.get(
    "/{alert_id}",
    response_model=AlertResponse,
    summary="Get alert",
    description="Get a single alert configuration by identifier.",
    responses={
        status.HTTP_200_OK: {"description": "Alert returned."},
        status.HTTP_404_NOT_FOUND: {"description": "Alert not found."},
    },
)
def get_alert(alert_id: int, service: AlertServiceDependency) -> AlertResponse:
    try:
        alert = service.get_alert(alert_id)
    except AlertNotFoundError as exc:
        raise _not_found_response(exc) from exc
    return AlertResponse.model_validate(alert)


@router.patch(
    "/{alert_id}",
    response_model=AlertResponse,
    summary="Update alert",
    description="Partially update an existing alert configuration.",
    responses={
        status.HTTP_200_OK: {"description": "Alert updated."},
        status.HTTP_404_NOT_FOUND: {"description": "Alert not found."},
        422: {"description": "Invalid alert update."},
    },
)
def update_alert(
    alert_id: int,
    payload: AlertUpdateRequest,
    service: AlertServiceDependency,
) -> AlertResponse:
    values: dict[str, Any] = payload.model_dump(exclude_unset=True)
    try:
        alert = service.update_alert(alert_id, values)
    except AlertNotFoundError as exc:
        raise _not_found_response(exc) from exc
    except AlertValidationError as exc:
        raise _validation_error_response(exc) from exc
    return AlertResponse.model_validate(alert)


@router.delete(
    "/{alert_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete alert",
    description="Delete an alert configuration.",
    responses={
        status.HTTP_204_NO_CONTENT: {"description": "Alert deleted."},
        status.HTTP_404_NOT_FOUND: {"description": "Alert not found."},
    },
)
def delete_alert(alert_id: int, service: AlertServiceDependency) -> Response:
    try:
        service.delete_alert(alert_id)
    except AlertNotFoundError as exc:
        raise _not_found_response(exc) from exc
    return Response(status_code=status.HTTP_204_NO_CONTENT)
