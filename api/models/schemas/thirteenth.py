from typing import Optional

from pydantic import BaseModel


class Thirteenth(BaseModel):
    raw: float
    earnings: Optional[float] = 0
    dependents: Optional[int] = 0
    months: int
    total: Optional[float]
