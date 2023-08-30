from lib.time_error import TimeError

def test_returns_difference_between_local_and_remote_times():
    time_error = TimeError()
    assert time_error.error() == 0.1