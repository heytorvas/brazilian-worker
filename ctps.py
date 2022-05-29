import json

INSS_DATA = json.load(open('inss.json', 'r'))
IRRF_DATA = json.load(open('irrf.json', 'r'))

def _find_percentage_and_deduction(data, salary):
    for percentage in data:
        if data[percentage]['min'] <= salary <= data[percentage]['max']:
            return percentage, data[percentage]['deduction']

def _calculate_inss_value(salary):
    percentage, deduction = _find_percentage_and_deduction(INSS_DATA, salary)
    if percentage == 'TETO':
        return 828.39
    return round(salary * (float(percentage)/100) - deduction, 2)

def _calculate_irrf_value(salary, inss):
    total = salary - inss
    percentage, deduction = _find_percentage_and_deduction(IRRF_DATA, total)
    return round(total * (float(percentage)/100) - deduction, 2)

def _calculate_fgts_value(salary):
    return round(salary * (8/100), 2)

def calculate_liquid_value(salary, earnings = 0, **kwargs):
    inss = _calculate_inss_value(salary)
    irrf = _calculate_irrf_value(salary, inss)
    discounts = sum([kwargs[i] for i in kwargs])
    total = round(salary + earnings - inss - irrf - discounts, 2)
    fgts = _calculate_fgts_value(salary)
    print(f'''
{' FOLHA DE PAGAMENTO '.center(30, '=')}
\nVencimentos:
\tSalário: {str(salary).rjust(5, ' ')}
\tAuxílio: {str(earnings).rjust(4, ' ')}
\nDescontos:
\tINSS: {str(inss).rjust(9, ' ')}
\tIRRF: {str(irrf).rjust(9, ' ')}
\tOutros: {str(discounts).rjust(7, ' ')}
\nFGTS: {str(fgts).rjust(6, ' ')}
\nTotal: {str(total).rjust(4, ' ')}
    ''')

salary = 2500
earnings = 150
calculate_liquid_value(salary, earnings, vr = 3.55, va = 1.5, am = 100)