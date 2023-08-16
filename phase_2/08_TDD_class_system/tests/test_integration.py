from lib.diary import Diary
from lib.diary_entry import DiaryEntry
"""
Adds two diary entries
I see them back in the list
"""

def test_adds_and_lists_diary_entries():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "My Contents 1")
    entry_2 = DiaryEntry("My Title 2", "My Contents 2")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.all() == [entry_1, entry_2]


"""
Given I add two diary entries 
And I call #count_words
I get the sum of all words in the contents of diary entries 
"""

def test_count_words_returns_count_of_all_words_in_all_entry_contents():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "one two three")
    entry_2 = DiaryEntry("My Title 2", "four five six")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.count_words() == 6


"""
Given I add two diary entries with total length of 5
And I call #reading_time with wpm of 2
Then total reading time should be 3
"""

def test_reading_time_returns_time_to_read_all_the_entries():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "one two")
    entry_2 = DiaryEntry("My Title 2", "three four five")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.reading_time(2) == 3


"""
GIven I add two diary entries, one long and one short 
And I call #find_best_entry_for_reading_time
With a wpm and minutes that means I can only read shor one 
THen #find_best_entry_for_reading_time returns the shorter one 
"""

def test_find_best_entry_for_reading_time_returns_entry_that_fits_in_time():
    diary = Diary()
    entry_1 = DiaryEntry("My Title 1", "one two")
    entry_2 = DiaryEntry("My Title 2", "one two three four five six seven")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_reading_time(2,3) 