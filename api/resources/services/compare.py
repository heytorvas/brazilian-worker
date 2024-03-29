from domain.models.clt import CLTBase
from domain.models.pj import PJBase
from domain.schemas.compare import CompareResponseSchema
from resources.services.clt import calculate_clt_salary_by_pj, calculate_liquid_value
from resources.services.pj import calculate_pj_salary, calculate_pj_salary_by_clt


def compare_clt_pj(input_clt, attachment):
    clt = calculate_liquid_value(input_clt, True)
    pj = calculate_pj_salary_by_clt(PJBase(raw=clt.total, attachment=attachment))
    return CompareResponseSchema(clt=clt, pj=pj)


def compare_pj_clt(input_pj):
    pj = calculate_pj_salary(input_pj)
    clt = calculate_clt_salary_by_pj(CLTBase(raw=pj.total))
    return CompareResponseSchema(clt=clt, pj=pj)
