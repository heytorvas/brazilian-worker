import json

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestIntegrationHour:
    URL = "/api/v1/hour"
    HEADERS = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }

    def test_calculate_salary_hour_without_daily_hours(self):
        body = {"raw": 3000, "weekly_hours": 40}
        response = json.loads(
            client.post(self.URL, headers=self.HEADERS, json=body).text
        )

        assert response["raw"] == 3000
        assert response["weekly_hours"] == 40
        assert response["daily_hours"] is None
        assert response["hour_value"] == 15
        assert response["day_value"] is None
        assert response["extra_hour_value"] == 22.5

    def test_calculate_salary_hour_with_daily_hours(self):
        body = {"raw": 3000, "weekly_hours": 40, "daily_hours": 8}
        response = json.loads(
            client.post(self.URL, headers=self.HEADERS, json=body).text
        )

        assert response["raw"] == 3000
        assert response["weekly_hours"] == 40
        assert response["daily_hours"] == 8
        assert response["hour_value"] == 15
        assert response["day_value"] == 120
        assert response["extra_hour_value"] == 22.5
