from domain.schemas.thirteenth import Thirteenth
from fastapi import APIRouter, Body
from resources.services.thirteenth import calculate_thirteenth

router = APIRouter()


@router.post('', response_model=Thirteenth)
def get_pj_salary(body: Thirteenth = Body(...)):
    return calculate_thirteenth(body)
