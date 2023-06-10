import pytest
import unittest.mock as mock
from bot.bot import TimeBot


@pytest.mark.asyncio
async def test_on_message():
    # Create a mock message object
    mock_message = mock.MagicMock()
    mock_message.author = mock.MagicMock()
    mock_message.author.nick = 'John'
    mock_message.author.name = 'John'
    mock_message.content = 'The time is 5:00 PM'
    mock_message.channel.send = mock.AsyncMock()

    # Mock the process_message method to return known data
    with mock.patch('bot.bot.process_message',
                    return_value=(True,
                                  {'author': 'John',
                                   'unix_timestamp': 1641027600})):

        # Stub the convert_to_utc_then_unix method to return the same timestamp
        with mock.patch('bot.helpers.convert_to_utc_then_unix',
                        return_value=1641027600):

            # Instantiate the TimeBot
            time_bot = TimeBot()

            # Mock the time_bot._connection.user
            time_bot._connection = mock.MagicMock()
            time_bot._connection.user = mock.MagicMock()

            # Execute the on_message method
            await time_bot.on_message(mock_message)

            # Assert if the channel.send method was called
            # with the expected message
            expected_msg = ('On John\'s message, that time would be: '
                            '<t:1641027600:t> on your local time zone.')
            mock_message.channel.send.assert_called_once_with(expected_msg)


@pytest.mark.asyncio
async def test_on_message_no_server_nickname():
    # Create a mock message object
    mock_message = mock.MagicMock()
    mock_message.author = mock.MagicMock()
    mock_message.author.nick = ''
    mock_message.author.name = 'John'
    mock_message.content = 'The time is 5:00 PM'
    mock_message.channel.send = mock.AsyncMock()

    # Mock the process_message method to return known data
    with mock.patch('bot.bot.process_message',
                    return_value=(True,
                                  {'author': 'John',
                                   'unix_timestamp': 1641027600})):

        # Stub the convert_to_utc_then_unix method to return the same timestamp
        with mock.patch('bot.helpers.convert_to_utc_then_unix',
                        return_value=1641027600):

            # Instantiate the TimeBot
            time_bot = TimeBot()

            # Mock the time_bot._connection.user
            time_bot._connection = mock.MagicMock()
            time_bot._connection.user = mock.MagicMock()

            # Execute the on_message method
            await time_bot.on_message(mock_message)

            # Assert if the channel.send method was called
            # with the expected message
            expected_msg = ('On John\'s message, that time would be: '
                            '<t:1641027600:t> on your local time zone.')
            mock_message.channel.send.assert_called_once_with(expected_msg)
