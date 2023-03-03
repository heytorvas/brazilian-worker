from enum import Enum

from pydantic import BaseModel, Field


class AttachmentEnum(str, Enum):
    I = 'I'
    II = 'II'
    III = 'III'
    IV = 'IV'
    V = 'V'


class PJBase(BaseModel):
    attachment: AttachmentEnum
    raw: float = Field(ge=0)


class PJ(PJBase):
    tax: float
    total: float
