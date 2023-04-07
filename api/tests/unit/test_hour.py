import pytest
from domain.models.hour import HourBase
from resources.services.hour import calculate_hour


class TestHourBaseModel:
    def test_create_valid_hour_base(self):
        hour = HourBase(raw=5000, weekly_hours=40)
        assert hour.raw == 5000
        assert hour.weekly_hours == 40
        assert hour.daily_hour is None

        hour = HourBase(raw="5000", weekly_hours="40", daily_hour="8")
        assert hour.raw == 5000
        assert hour.weekly_hours == 40
        assert hour.daily_hour == 8

    def test_create_invalid_hour_base(self):
        with pytest.raises(ValueError):
            HourBase(raw="opa", weekly_hours=40)
        with pytest.raises(ValueError):
            HourBase(raw=5000, weekly_hours="opa")
        with pytest.raises(ValueError):
            HourBase(raw=5000, weekly_hours=40, daily_hour="opa")


class TestHourModel:
    def test_check_without_daily_hour_should_return_none(self):
        base = HourBase(raw=5000, weekly_hours=40)
        hour = calculate_hour(base)
        assert base.daily_hour is None
        assert hour.day_value is None
