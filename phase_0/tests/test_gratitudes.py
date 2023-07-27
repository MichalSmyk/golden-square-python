from lib.gratitudes import *

#returns empty array of gratitudes
def test_initializes_with_empty_array():
    gratitudes = Gratitudes()
    assert gratitudes.format() == "Be grateful for: "

#adds one gratitude
def test_adds_one_gratitude():
    gratitudes = Gratitudes()
    gratitudes.add("weather")
    assert gratitudes.format() == "Be grateful for: weather"