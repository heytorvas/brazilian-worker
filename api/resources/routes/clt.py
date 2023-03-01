from domain.models.clt import CLT, CLTBase
from fastapi import APIRouter, Body
from resources.services.clt import calculate_liquid_value

router = APIRouter()


@router.post('', response_model=CLT, response_model_exclude_none=True)
def get_salary_liquid(salary: CLTBase = Body(...)):
    return calculate_liquid_value(salary)
