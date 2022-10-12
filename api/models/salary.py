from typing import Optional

from pydantic import BaseModel


class SalaryBase(BaseModel):
    raw: float
    earnings: Optional[float] = 0
    medical_assistant: Optional[float] = 0
    discounts: Optional[float] = 0


class Salary(SalaryBase):
    inss: float
    irrf: float
    fgts: float
    total: float
