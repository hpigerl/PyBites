from pytz import timezone, utc
import datetime

AUSTRALIA = timezone("Australia/Sydney")
SPAIN = timezone("Europe/Madrid")


def what_time_lives_pybites(naive_utc_dt: datetime.datetime):
    """Receives a naive UTC datetime object and returns a two element
    tuple of Australian and Spanish (timezone aware) datetimes"""
    aware_utc_dt = utc.localize(naive_utc_dt)
    return (aware_utc_dt.astimezone(AUSTRALIA), aware_utc_dt.astimezone(SPAIN))
