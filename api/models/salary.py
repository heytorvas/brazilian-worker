from typing import Optional, Union

from pydantic import BaseModel


class SalaryBase(BaseModel):
    raw: float
    earnings: Optional[float] = 0
    medical_assistant: Optional[float] = 0
    discounts: Optional[float] = 0
    dependents: Optional[int] = 0
    transport_voucher: Union[bool, float] = False

class Salary(SalaryBase):
    inss: float
    irrf: float
    fgts: float
    total: float
