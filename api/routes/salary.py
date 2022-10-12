from api.models.salary import SalaryBase
from api.services.salary import calculate_liquid_value
from fastapi import APIRouter, Body

router = APIRouter()

@router.post('/')
def get_salary_liquid(salary: SalaryBase = Body(...)):
    return calculate_liquid_value(salary)
