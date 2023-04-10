export interface HourBase {
    raw: number;
    weekly_hours: number;
    daily_hours: number;
}

export interface Hour extends HourBase {
    hour_value: number;
    day_value: number;
    extra_hour_value: number;
}