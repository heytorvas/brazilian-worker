import json

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestIntegrationSalary:

    URL = '/api/v1/salary/'
    HEADERS = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    def test_calculate_liquid_salary_only_raw(self):
        body = {'raw': 3000}
        response = json.loads(
            client.post(self.URL, headers=self.HEADERS, json=body).text
        )

        assert response['raw'] == 3000
        assert response['discounts'] == 0
        assert response['earnings'] == 0
        assert response['dependents'] == 0
        assert response['transport_voucher'] == 0
        assert response['medical_assistant'] == 0
        assert response['fgts'] == 240
        assert response['inss'] == 269
        assert response['irrf'] == 62.02
        assert response['total'] == 2668.98

    def test_calculate_liquid_salary_with_raw_and_transport_voucher(self):
        body = {'raw': 3000, 'transport_voucher': True}
        response = json.loads(
            client.post(self.URL, headers=self.HEADERS, json=body).text
        )

        assert response['raw'] == 3000
        assert response['earnings'] == 0
        assert response['medical_assistant'] == 0
        assert response['discounts'] == 0
        assert response['dependents'] == 0
        assert response['transport_voucher'] == 180
        assert response['inss'] == 269
        assert response['irrf'] == 62.02
        assert response['fgts'] == 240
        assert response['total'] == 2488.98

    def test_calculate_liquid_salary_with_dependents(self):
        body = {'raw': 3000, 'dependents': 1, 'transport_voucher': True}
        response = json.loads(
            client.post(self.URL, headers=self.HEADERS, json=body).text
        )

        assert response['raw'] == 3000
        assert response['earnings'] == 0
        assert response['medical_assistant'] == 0
        assert response['discounts'] == 0
        assert response['dependents'] == 1
        assert response['transport_voucher'] == 180
        assert response['inss'] == 269
        assert response['irrf'] == 47.81
        assert response['fgts'] == 240
        assert response['total'] == 2503.19
