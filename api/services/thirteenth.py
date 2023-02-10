from models.clt import CLTBase
from services.clt import calculate_liquid_value


def calculate_thirteenth(input):
    raw = ((input.raw + input.earnings) / 12) * input.months
    clt = CLTBase(raw=raw, dependents=input.dependents)
    input.total = calculate_liquid_value(clt).total
    return input
