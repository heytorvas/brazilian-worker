from enum import Enum

from pydantic import BaseModel


class AttachEnum(str, Enum):
    I = 'I'
    II = 'II'
    III = 'III'
    IV = 'IV'
    V = 'V'


class PJBase(BaseModel):
    attach: AttachEnum
    raw: float


class PJ(PJBase):
    tax: float
    total: float
