from datetime import datetime

import pytz
from tzlocal import get_localzone

__all__ = ['convert_to_utc_then_unix']


def convert_to_utc_then_unix(time_str: str):
    # Getting local tz and getting current time from tz
    local_tz = get_localzone()
    current_datetime = datetime.now(local_tz)

    # Converting time string to local datetime
    time_obj = datetime.strptime(time_str, '%I:%M %p')
    local_datetime = current_datetime.replace(
        hour=time_obj.hour, minute=time_obj.minute,
        second=0, microsecond=0
    )

    # Converting local datetime to UTC datetime
    utc_datetime = local_datetime.astimezone(pytz.UTC)

    # Generate UNIX timestamp
    unix_timestamp = int(utc_datetime.timestamp())

    return unix_timestamp
