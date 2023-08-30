from lib.time_error import TimeError
from unittest.mock import Mock

def test_returns_difference_between_local_and_remote_times():
    requester_mock = Mock()
    response_mock = Mock()
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {"unixtime": 1693400891}
    timer_mock = Mock()
    timer_mock.time.return_value = 1693401132.5
    time_error = TimeError(requester_mock, timer_mock)
    assert time_error.error() == -241.5