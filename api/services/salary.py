import json

from models.salary import Salary

INSS_DATA = json.load(open('data/inss.json', 'r'))
IRRF_DATA = json.load(open('data/irrf.json', 'r'))

def _find_percentage_and_deduction(data, salary):
    for percentage in data:
        if data[percentage]['min'] <= salary <= data[percentage]['max']:
            return percentage, data[percentage]['deduction']

def _calculate_inss_value(salary):
    percentage, deduction = _find_percentage_and_deduction(INSS_DATA, salary)
    if percentage == 'TETO':
        return deduction
    return round(salary * (float(percentage)/100) - deduction, 2)

def _calculate_irrf_value(salary, inss):
    total = salary - inss
    percentage, deduction = _find_percentage_and_deduction(IRRF_DATA, total)
    return round(total * (float(percentage)/100) - deduction, 2)

def _calculate_fgts_value(salary):
    return round(salary * (8/100), 2)

def calculate_liquid_value(input):
    discounts = input.discounts + input.medical_assistant
    inss = _calculate_inss_value(input.raw)
    irrf = _calculate_irrf_value(input.raw, inss)
    total = round(input.raw + input.earnings - inss - irrf - discounts, 2)
    return Salary(
        raw=input.raw,
        earnings=input.earnings,
        medical_assistant=input.medical_assistant,
        discounts=input.discounts,
        inss=inss,
        irrf=irrf,
        fgts=_calculate_fgts_value(input.raw),
        total=total
    )
