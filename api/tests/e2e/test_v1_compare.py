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
        assert response["clt"]["irrf"] == 831.19
        assert response["clt"]["fgts"] == 560
        assert response["clt"]["thirteenth"] == 446.05
        assert response["clt"]["vacation"] == 586.29
        assert response["clt"]["total"] == 6944.97

        assert response["pj"]["raw"] == 7234.34
        assert response["pj"]["attachment"] == "I"
        assert response["pj"]["tax"] == 289.37
        assert response["pj"]["total"] == 6944.97

    def test_compare_pj_clt_salary(self):
        body = {"attachment": "V", "raw": 14000}
        response = json.loads(
            client.post(f"{self.URL}/pj", headers=self.HEADERS, json=body).text
        )

        assert response["clt"]["raw"] == 12174.1
        assert response["clt"]["inss"] == 828.39
        assert response["clt"]["irrf"] == 2250.71
        assert response["clt"]["fgts"] == 973.93
        assert response["clt"]["total"] == 11829.94
        assert response["clt"]["vacation"] == 1003.09
        assert response["clt"]["thirteenth"] == 757.92

        assert response["pj"]["attachment"] == "V"
        assert response["pj"]["raw"] == 14000
        assert response["pj"]["tax"] == 2170
        assert response["pj"]["total"] == 11830
