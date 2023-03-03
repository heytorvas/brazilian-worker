import json

from domain.models.pj import PJ
from exceptions import MaximumRawSalaryReachedException

PJ_DATA = json.load(open('data/pj.json', 'r'))


def _find_percentage_and_deduction(attachment, salary):
    salary = _calculate_salary_per_year(salary)
    for index in PJ_DATA[attachment]:
        if index['min'] <= salary <= index['max']:
            return index['percent'], index['deduction']

    raise MaximumRawSalaryReachedException('Maximum PJ raw salary reached.')


def _calculate_salary_per_year(raw):
    return raw * 12


def _get_tax_value(attachment, raw):
    percentage, deduction = _find_percentage_and_deduction(attachment, raw)
    return round(raw * (percentage / 100) - (deduction / 12), 2)


def calculate_pj_salary(input):
    tax = _get_tax_value(input.attachment, input.raw)
    return PJ(
        attachment=input.attachment,
        raw=input.raw,
        tax=tax,
        total=round(input.raw - tax, 2),
    )


def calculate_pj_salary_by_clt(input):
    pj = None
    raw_clone = input.raw

    while True:
        aux = calculate_pj_salary(input)
        if aux.total != raw_clone:
            input.raw = round(input.raw + 0.01, 2)
        else:
            pj = aux
            break

    return pj
