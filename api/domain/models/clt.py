from typing import Optional, Union

from pydantic import BaseModel, Field


class CLTBase(BaseModel):
    raw: float = Field(ge=0)
    earnings: Optional[float] = Field(0, ge=0)
    medical_assistant: Optional[float] = Field(0, ge=0)
    discounts: Optional[float] = Field(0, ge=0)
    dependents: Optional[int] = Field(0, ge=0)
    transport_voucher: Union[float, bool] = Field(0, ge=0)


class CLT(CLTBase):
    inss: float
    irrf: float
    fgts: float
    total: float
    vacation: Optional[float] = None
    thirteenth: Optional[float] = None
