import json

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestIntegrationCompare:
    URL = '/api/v1/compare/'
    HEADERS = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    def test_compare_clt_pj_salary(self):
        body = {'raw': 7000, 'attachment': 'I'}
        response = json.loads(
            client.post(self.URL, headers=self.HEADERS, json=body).text
        )

        assert response['clt']['raw'] == 7000
        assert response['clt']['inss'] == 816.18
        assert response['clt']['irrf'] == 831.19
        assert response['clt']['fgts'] == 560
        assert response['clt']['thirteenth'] == 583.33
        assert response['clt']['vacation'] == 583.33
        assert response['clt']['vacation_one_third'] == 194.44
        assert response['clt']['total'] == 7273.73

        assert response['pj']['raw'] == 7576.80
        assert response['pj']['attachment'] == 'I'
        assert response['pj']['tax'] == 303.07
        assert response['pj']['total'] == 7273.73
