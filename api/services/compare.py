from models.pj import PJBase
from models.schemas.compare import CompareResponseSchema
from services.clt import calculate_liquid_value
from services.pj import calculate_pj_salary_by_clt


def compare_clt_pj(input_clt, attachment):
    clt = calculate_liquid_value(input_clt, True)
    pj = calculate_pj_salary_by_clt(PJBase(raw=clt.total, attachment=attachment))
    return CompareResponseSchema(clt=clt, pj=pj)
