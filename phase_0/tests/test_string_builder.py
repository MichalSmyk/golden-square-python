from lib.string_builder import *

#starts with empty string
def test_string_builder_init_with_empty_string():
    builder = StringBuilder()
    assert builder.output() == ""
#length for empty string
def test_length_of_empty_string_is_zero():
    builder = StringBuilder()
    assert builder.size() == 0
#adds string
def test_adds_to_the_string():
    builder = StringBuilder()
    builder.add(" Mike")
    assert builder.size() == 5
    assert builder.output() == " Mike"
#adds strings 
def test_adds_two_strings():
    builder = StringBuilder()
    builder.add("Soft")
    builder.add("ware")
    assert builder.size() == 8
    assert builder.output() == "Software"