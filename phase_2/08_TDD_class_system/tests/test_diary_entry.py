from lib.diary_entry import DiaryEntry

"""
When I initialise with a title and contents
I can get a title and contents back
"""

def test_constructs_and_gets_title_and_contents():
    diary_entry = DiaryEntry("My title", "My Contents")
    assert diary_entry.title == "My title"
    assert diary_entry.contents == "My Contents"
