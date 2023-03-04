import json

from domain.models.clt import CLT, CLTBase
from exceptions import MaximumRawSalaryReachedException

INSS_DATA = json.load(open("data/inss.json", "r"))
IRRF_DATA = json.load(open("data/irrf.json", "r"))
VALUE_PER_DEPENDENT = 189.59


def _find_percentage_and_deduction(data, salary):
    for percentage in data:
        if data[percentage]["min"] <= salary <= data[percentage]["max"]:
            return percentage, data[percentage]["deduction"]

    raise MaximumRawSalaryReachedException("Maximum CLT raw salary reached.")


def _calculate_inss_value(salary):
    percentage, deduction = _find_percentage_and_deduction(INSS_DATA, salary)
    if percentage == "TETO":
        return deduction
    return round(salary * (float(percentage) / 100) - deduction, 2)


def _calculate_irrf_value(salary, inss, dependents):
    total = salary - inss - (dependents * VALUE_PER_DEPENDENT)
    percentage, deduction = _find_percentage_and_deduction(IRRF_DATA, total)
    return round(total * (float(percentage) / 100) - deduction, 2)


def _calculate_fgts_value(salary):
    return round(salary * (8 / 100), 2)


def _calculate_transport_voucher(salary, condition):
    if json.loads(str(condition).lower()):
        return round(salary * (6 / 100), 2)
    return 0


def _calculate_vacation(salary):
    salary = calculate_liquid_value(CLTBase(raw=salary + (salary * (1 / 3))))
    return round(salary.total * (1 / 12), 2)


def _calculate_vacation_one_third(vacation):
    salary = calculate_liquid_value(CLTBase(raw=vacation))
    return round(salary.total * (1 / 12), 2)


def calculate_liquid_value(input, pj=False):
    discounts = input.discounts + input.medical_assistant
    transport_voucher = _calculate_transport_voucher(input.raw, input.transport_voucher)
    inss = _calculate_inss_value(input.raw)
    irrf = _calculate_irrf_value(input.raw, inss, input.dependents)
    total = round(
        input.raw + input.earnings - inss - irrf - discounts - transport_voucher, 2
    )
    clt = CLT(
        raw=input.raw,
        earnings=input.earnings,
        medical_assistant=input.medical_assistant,
        discounts=input.discounts,
        dependents=input.dependents,
        transport_voucher=transport_voucher,
        inss=inss,
        irrf=irrf,
        fgts=_calculate_fgts_value(input.raw),
        total=total,
    )
    if pj:
        clt.vacation = _calculate_vacation(clt.raw)
        clt.thirteenth = _calculate_vacation_one_third(clt.raw)
        clt.total = round(
            sum(
                [
                    clt.total,
                    clt.vacation,
                    clt.thirteenth,
                    clt.fgts,
                ]
            ),
            2,
        )
        return clt

    return clt


def calculate_clt_salary_by_pj(input):
    clt = None
    raw_clone = input.raw

    while True:
        aux = calculate_liquid_value(input, True)
        if aux.total < raw_clone:
            input.raw = round(input.raw + 1.00, 2)
        else:
            while True:
                aux = calculate_liquid_value(input, True)
                if aux.total > raw_clone:
                    input.raw = round(input.raw - 0.01, 2)
                else:
                    clt = aux
                    break
            break

    return clt
