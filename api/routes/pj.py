from fastapi import APIRouter, Body
from models.pj import PJ, PJBase
from services.pj import calculate_pj_salary

router = APIRouter()


@router.post('/', response_model=PJ)
def get_pj_salary(body: PJBase = Body(...)):
    return calculate_pj_salary(body)
