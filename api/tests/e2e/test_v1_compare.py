import json

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestIntegrationCompare:
    URL = '/api/v1/compare'
    HEADERS = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    def test_compare_clt_pj_salary(self):
        body = {'raw': 7000, 'attachment': 'I'}
        response = json.loads(
            client.post(f'{self.URL}/clt', headers=self.HEADERS, json=body).text
        )

        assert response['clt']['raw'] == 7000
        assert response['clt']['inss'] == 816.18
        assert response['clt']['irrf'] == 831.19
        assert response['clt']['fgts'] == 560
        assert response['clt']['thirteenth'] == 446.05
        assert response['clt']['vacation'] == 446.05
        assert response['clt']['vacation_one_third'] == 12.39
        assert response['clt']['total'] == 6817.12

        assert response['pj']['raw'] == 7101.17
        assert response['pj']['attachment'] == 'I'
        assert response['pj']['tax'] == 284.05
        assert response['pj']['total'] == 6817.12

    def test_compare_pj_clt_salary(self):
        body = {'attachment': 'V', 'raw': 14000}
        response = json.loads(
            client.post(f'{self.URL}/pj', headers=self.HEADERS, json=body).text
        )

        assert response['clt']['raw'] == 12415.81
        assert response['clt']['inss'] == 828.39
        assert response['clt']['irrf'] == 2317.18
        assert response['clt']['fgts'] == 993.26
        assert response['clt']['total'] == 11830
        assert response['clt']['vacation'] == 772.52
        assert response['clt']['vacation_one_third'] == 21.46
        assert response['clt']['thirteenth'] == 772.52

        assert response['pj']['attachment'] == 'V'
        assert response['pj']['raw'] == 14000
        assert response['pj']['tax'] == 2170
        assert response['pj']['total'] == 11830
