from fastapi.testclient import TestClient

from miles_app.main import create_app


def test_openapi_includes_frontend_mvp_contract_paths() -> None:
    # Arrange
    client = TestClient(create_app())

    # Act
    response = client.get("/openapi.json")
    paths = response.json()["paths"]

    # Assert
    assert response.status_code == 200
    assert "/alerts" in paths
    assert "/alerts/{alert_id}" in paths
    assert "/opportunities" in paths
    assert "/opportunities/{opportunity_id}" in paths
    assert "/feedback" in paths
    assert "/feedback/summary" in paths
    assert "/notifications" in paths
    assert "/notifications/{notification_id}/status" in paths
    assert "/health" in paths


def test_placeholder_opportunities_contract_returns_empty_collection_and_404() -> None:
    # Arrange
    client = TestClient(create_app())

    # Act
    list_response = client.get("/opportunities")
    detail_response = client.get("/opportunities/1")

    # Assert
    assert list_response.status_code == 200
    assert list_response.json() == []
    assert detail_response.status_code == 404
    assert "persistence is not implemented" in detail_response.json()["detail"]


def test_placeholder_feedback_contract_accepts_payload_and_returns_zero_summary() -> None:
    # Arrange
    client = TestClient(create_app())
    payload = {
        "user_id": 1,
        "alert_id": 1,
        "opportunity_id": 1,
        "feedback_type": "notification_relevance",
        "rating": 4,
        "reason": "too_expensive",
        "comment": "Good route, but the fees were higher than expected.",
    }

    # Act
    create_response = client.post("/feedback", json=payload)
    summary_response = client.get("/feedback/summary")

    # Assert
    assert create_response.status_code == 202
    assert create_response.json()["status"] == "accepted_placeholder"
    assert create_response.json()["feedback"] == payload
    assert summary_response.status_code == 200
    assert summary_response.json() == {
        "total_feedback": 0,
        "useful_count": 0,
        "not_useful_count": 0,
        "top_reasons": [],
    }


def test_placeholder_notifications_contract_returns_empty_collection_and_404() -> None:
    # Arrange
    client = TestClient(create_app())

    # Act
    list_response = client.get("/notifications", params={"user_id": 1})
    update_response = client.patch("/notifications/1/status", json={"status": "opened"})

    # Assert
    assert list_response.status_code == 200
    assert list_response.json() == []
    assert update_response.status_code == 404
    assert "persistence is not implemented" in update_response.json()["detail"]
