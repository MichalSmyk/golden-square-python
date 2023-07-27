from lib.greet import *

def test_greets_user():
    result = greet("Mike")
    assert result == "Hello, Mike!"