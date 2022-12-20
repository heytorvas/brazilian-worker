import json

from models.pj import PJ

PJ_DATA = json.load(open('data/pj.json', 'r'))


def _find_percentage_and_deduction(attach, salary):
    salary = _calculate_salary_per_year(salary)
    for index in PJ_DATA[attach]:
        if index['min'] <= salary <= index['max']:
            return index['percent'], index['deduction']


def _calculate_salary_per_year(raw):
    return raw * 12


def _get_tax_value(attach, raw):
    percentage, deduction = _find_percentage_and_deduction(attach, raw)
    return round(raw * (percentage / 100) - (deduction / 12), 2)


def calculate_pj_salary(input):
    tax = _get_tax_value(input.attach, input.raw)
    return PJ(attach=input.attach, raw=input.raw, tax=tax, total=input.raw - tax)
