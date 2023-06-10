import re
from datetime import datetime

import pytz
from tzlocal import get_localzone

# Define regular expression pattern to find time information
time_pattern = re.compile(r'\b\d{1,2}:\d{2}\s*(?:AM|PM)?\b', re.IGNORECASE)


def process_message(author: str, content: str):
    # Extract time from the message
    match = time_pattern.search(content)
    if match:
        time_string = match.group()

        # Get the local time zone
        local_tz = get_localzone()

        # Convert time string to local datetime
        current_datetime = datetime.now(local_tz)
        time_obj = datetime.strptime(time_string, '%I:%M %p')
        local_datetime = current_datetime.replace(
            hour=time_obj.hour, minute=time_obj.minute, second=0, microsecond=0
        )

        # Convert local datetime to UTC datetime
        utc_datetime = local_datetime.astimezone(pytz.UTC)

        # Generate UNIX timestamp
        unix_timestamp = int(utc_datetime.timestamp())

        # Construct a response message
        response = (
            f'On {author}\'s message, that time will be: '
            f'<t:{unix_timestamp}:t>.'
        )
        return response

    return None
