from typing import Optional, Union

from pydantic import BaseModel


class CLTBase(BaseModel):
    raw: float
    earnings: Optional[float] = 0
    medical_assistant: Optional[float] = 0
    discounts: Optional[float] = 0
    dependents: Optional[int] = 0
    transport_voucher: Union[float, bool] = 0


class CLT(CLTBase):
    inss: float
    irrf: float
    fgts: float
    total: float
    vacation: Optional[float] = None
    thirteenth: Optional[float] = None
