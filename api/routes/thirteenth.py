from fastapi import APIRouter, Body
from models.schemas.thirteenth import Thirteenth
from services.thirteenth import calculate_thirteenth

router = APIRouter()


@router.post('', response_model=Thirteenth)
def get_pj_salary(body: Thirteenth = Body(...)):
    return calculate_thirteenth(body)
