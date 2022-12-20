import re

import requests
from bs4 import BeautifulSoup


def _formatter_currency(value):
    return float(value.replace(".", "").replace(",", "."))


def _formatter_value_from_table(row):
    values = [_formatter_currency(item) for item in re.findall(r'[\d]+[.,\d]+', row)]
    return {
        "min": 0 if len(values) == 1 else values[0],
        "max": values[0] if len(values) == 1 else values[1],
    }


def _formatter_others_values(value):
    string = re.findall(r'[\d]+[.,\d]+', value)
    return float(string[0].replace(".", "").replace(",", ".")) if len(string) > 0 else 0


def get_html_body():
    r = requests.get(
        'https://www.contabilizei.com.br/contabilidade-online/tabela-simples-nacional-completa/'
    ).text
    soup = BeautifulSoup(r, 'html.parser')
    body = soup.find('body')
    return body.find_all('figure', {'class': 'wp-block-table'})


def get_all_attachments():
    tables = get_html_body()
    attachments = ['I', 'II', 'III', 'IV', 'V']
    response = {}
    for j in range(5):
        rows = tables[j].find_all('tr')

        aux = []
        for i in range(1, len(rows)):
            tds = rows[i].find_all('td')
            row = {
                "percent": _formatter_others_values(tds[1].text),
                "deduction": _formatter_others_values(tds[2].text),
            }
            row.update(_formatter_value_from_table(tds[0].text))
            aux.append(row)

        response.update({attachments[j]: aux})
    return response
