import json

from models.pj import PJ

PJ_DATA = json.load(open('data/pj.json', 'r'))


def _find_percentage_and_deduction(attachment, salary):
    salary = _calculate_salary_per_year(salary)
    for index in PJ_DATA[attachment]:
        if index['min'] <= salary <= index['max']:
            return index['percent'], index['deduction']


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
    raw_clone = input.raw
    percentage, deduction = _find_percentage_and_deduction(input.attachment, input.raw)

    total = input.raw + (input.raw * (percentage / 100))
    total = total + (deduction / 12)
    input.raw = total

    pj = calculate_pj_salary(input)

    while True:
        aux = calculate_pj_salary(input)
        if aux.total != raw_clone:
            input.raw = round(input.raw + 0.01, 2)
        else:
            pj = aux
            break

    return pj
