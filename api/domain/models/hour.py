from typing import Optional

from pydantic import BaseModel, Field


class HourBase(BaseModel):
    raw: float = Field(ge=0)
    weekly_hours: int = Field(ge=0)
    daily_hour: Optional[int] = Field(None, ge=0)


class Hour(HourBase):
    hour_value: float
    day_value: Optional[float] = None
    extra_hour_value: Optional[float] = None
