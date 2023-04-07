from domain.models.hour import Hour, HourBase
from fastapi import APIRouter, Body
from resources.services.hour import calculate_hour

router = APIRouter()


@router.post("", response_model=Hour)
def get_hour_value(body: HourBase = Body(...)):
    return calculate_hour(body)
