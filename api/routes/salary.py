from fastapi import APIRouter, Body
from models.salary import SalaryBase
from services.salary import calculate_liquid_value

router = APIRouter()

@router.post('/')
def get_salary_liquid(salary: SalaryBase = Body(...)):
    return calculate_liquid_value(salary)
