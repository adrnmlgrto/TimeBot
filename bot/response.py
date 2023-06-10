import re
from typing import Tuple, Union

from bot.helpers import convert_to_utc_then_unix

# Define regular expression pattern to find time information
time_pattern = re.compile(r'\b\d{1,2}:\d{2}\s*(?:AM|PM)?\b', re.IGNORECASE)


def process_message(author: str,
                    content: str) -> Tuple[bool, Union[dict, str]]:
    # Extract time from the message
    match = time_pattern.search(content)
    if match:
        time_string = match.group()

        # Generate UNIX time for response
        unix_timestamp = convert_to_utc_then_unix(time_str=time_string)

        # Construct a response message
        response = True, {
            'author': author,
            'unix_timestamp': unix_timestamp,
            'original_time_string': time_string
        }
        return response

    return False, ''
