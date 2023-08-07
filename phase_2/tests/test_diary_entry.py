from lib.diary_entry import DiaryEntry
import pytest

"""
Given a title and contents 
#fotmat returns a formatted entry like:
"My title: THese are the contents"
"""

def test_formats_with_title_and_contents():
    diary_entry = DiaryEntry("My title", "Some contents")
    result = diary_entry.format()
    assert result == "My title: Some contents"


"""
Given a title and contents 
#count_words returns the number of words in title and contents 
"""
def test_counts_words_in_both_title_and_contents():
    diary_entry = DiaryEntry("My title", "Some contents")
    result = diary_entry.count_words()
    assert result == 4

"""
Given an empty title and contents
Raises an error 
"""

def test_errors_on_empty_title_and_contents():
    with pytest.raises(Exception) as err:
        DiaryEntry("","")
    assert str(err.value) == "Diary entries must have a title or content"

"""
Given a wpm of 2
and a text with 2 words
#reading_time returns one minute
"""

def test_reading_time_with_two_wpm_and_two_words():
    diary_entry = DiaryEntry("My title", "Some contents")
    result = diary_entry.reading_time(2)
    assert result == 1

"""
Given a wpm of 2
and a text with 4 words
#reading_time returns 2 minutes
"""

def test_reading_time_with_two_wpm_and_two_words():
    diary_entry = DiaryEntry("My title", "Some contents")
    result = diary_entry.reading_time(4)
    assert result == 2