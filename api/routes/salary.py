from fastapi import APIRouter, Body
from models.clt import CLTBase
from services.salary import calculate_liquid_value

router = APIRouter()


@router.post('/')
def get_salary_liquid(salary: CLTBase = Body(...)):
    return calculate_liquid_value(salary)
