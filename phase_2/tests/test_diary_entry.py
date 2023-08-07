from lib.diary_entry import DiaryEntry

"""
Given a title and contents 
#fotmat returns a formatted entry like:
"My title: THese are the contents"
"""

def test_formats_with_title_and_contents():
    diary_entry = DiaryEntry("My title", "Some contents")
    result = diary_entry.format()
    assert result == "My title: Some contents"

    