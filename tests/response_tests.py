import pytest
from bot.response import process_message
from bot.helpers.convert import convert_to_utc_then_unix
from freezegun import freeze_time


@pytest.mark.parametrize('author, content, time_str, expected_status', [
    ('John', 'The time is 5:00 PM', '5:00 PM', True),
    ('Alice', 'It\'s 10:30 AM', '10:30 AM', True),
    ('Bob', 'No time mentioned', '', False),
])
@freeze_time('2022-01-01 12:00:00')
def test_process_message(author, content, time_str, expected_status):
    status, data = process_message(author, content)

    if expected_status:
        expected_unix_timestamp = convert_to_utc_then_unix(time_str)
        expected_data = {
            'author': author,
            'unix_timestamp': expected_unix_timestamp
        }
    else:
        expected_data = ''

    assert status == expected_status
    assert data == expected_data
