import json

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestIntegrationPJ:
    URL = '/api/v1/pj'
    HEADERS = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    def test_get_pj_liquid_salary(self):
        body = {'raw': 7576.80, 'attachment': 'I'}
        response = json.loads(
            client.post(self.URL, headers=self.HEADERS, json=body).text
        )

        assert response['raw'] == 7576.80
        assert response['attachment'] == 'I'
        assert response['tax'] == 303.07
        assert response['total'] == 7273.73
