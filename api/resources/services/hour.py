from domain.models.hour import Hour


def calculate_salary_hour(input):
    return round(input.raw / (input.weekly_hours * 5), 2)


def calculate_salary_day(hour_value, daily_hours):
    return round(hour_value * daily_hours, 2)


def calculate_extra_hour(hour_value):
    return round(hour_value + (hour_value * (50 / 100)), 2)


def calculate_hour(input):
    hour_value = calculate_salary_hour(input)
    return Hour(
        raw=input.raw,
        weekly_hours=input.weekly_hours,
        daily_hours=input.daily_hours,
        hour_value=hour_value,
        day_value=calculate_salary_day(hour_value, input.daily_hours)
        if input.daily_hours
        else None,
        extra_hour_value=calculate_extra_hour(hour_value),
    )
