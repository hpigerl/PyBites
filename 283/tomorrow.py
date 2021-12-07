from datetime import datetime, timedelta
from typing import Optional


def tomorrow(date_today: Optional[datetime] = None):
    if date_today is None:
        date_today = datetime.today()
    tmr = date_today + timedelta(days=1)
    if hasattr(tmr, "hour"):
        tmr = tmr.date()
    return tmr
