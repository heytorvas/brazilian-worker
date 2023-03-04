import json

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestIntegrationThirteenth:
    URL = "/api/v1/thirteenth"
    HEADERS = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }

    def test_calculate_thirteenth_full(self):
        body = {"raw": 5000, "months": 12}
        response = json.loads(
            client.post(self.URL, headers=self.HEADERS, json=body).text
        )

        assert response["raw"] == 5000
        assert response["months"] == 12
        assert response["total"] == 4095.59

    def test_calculate_thirteenth_partitioned(self):
        body = {"raw": 5000, "months": 10}
        response = json.loads(
            client.post(self.URL, headers=self.HEADERS, json=body).text
        )

        assert response["raw"] == 5000
        assert response["months"] == 10
        assert response["total"] == 3539.89
