import json

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestIntegrationCompare:
    URL = "/api/v1/compare"
    HEADERS = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }

    def test_compare_clt_pj_salary(self):
        body = {"raw": 7000, "attachment": "I"}
        response = json.loads(
            client.post(f"{self.URL}/clt", headers=self.HEADERS, json=body).text
        )

        assert response["clt"]["raw"] == 7000
        assert response["clt"]["inss"] == 816.18
        assert response["clt"]["irrf"] == 815.59
        assert response["clt"]["fgts"] == 560
        assert response["clt"]["thirteenth"] == 447.35
        assert response["clt"]["vacation"] == 587.59
        assert response["clt"]["total"] == 6963.17

        assert response["pj"]["raw"] == 7253.3
        assert response["pj"]["attachment"] == "I"
        assert response["pj"]["tax"] == 290.13
        assert response["pj"]["total"] == 6963.17

    def test_compare_pj_clt_salary(self):
        body = {"attachment": "V", "raw": 14000}
        response = json.loads(
            client.post(f"{self.URL}/pj", headers=self.HEADERS, json=body).text
        )

        assert response["clt"]["raw"] == 12154.90
        assert response["clt"]["inss"] == 828.39
        assert response["clt"]["irrf"] == 2229.83
        assert response["clt"]["fgts"] == 972.39
        assert response["clt"]["total"] == 11829.97
        assert response["clt"]["vacation"] == 1002.84
        assert response["clt"]["thirteenth"] == 758.06

        assert response["pj"]["attachment"] == "V"
        assert response["pj"]["raw"] == 14000
        assert response["pj"]["tax"] == 2170
        assert response["pj"]["total"] == 11830
