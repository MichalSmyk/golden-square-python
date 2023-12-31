from lib.diary_entry import DiaryEntry

"""
When I initialise with a title and contents
I can get a title and contents back
"""

def test_constructs_and_gets_title_and_contents():
    diary_entry = DiaryEntry("My title", "My Contents")
    assert diary_entry.title == "My title"
    assert diary_entry.contents == "My Contents"

"""
When I initialise with five-word contents
Then #count_words should return 5
"""

def test_count_words_returns_word_count_of_contents():
    diary_entry = DiaryEntry("My title", "one two three four five")
    assert diary_entry.count_words() == 5


"""
When I initialize with five word contents
then #reading_time with a wpm of 2 should return 3
"""
def test_reading_time():
    diary_entry = DiaryEntry("My title", "one two three four five")    
    assert diary_entry.reading_time(2) == 3

"""
When I initialise with a five work contents
Then, at first #readin_chunk should return the first chunk
readable in the time 
"""

def test_readable_chunk_first_chunk():
    diary_entry = DiaryEntry("My title", "one two three four five")
    assert diary_entry.reading_chunk(2, 1) == ("one two")


"""
When I initialize with a five-word contents
Then, on the second call, #reading+chunk should retiurn th esecond chunk 
readable in the time
"""

def test_readable_chunk_second_chunk():
    diary_entry = DiaryEntry("My title", "one two three four five")
    diary_entry.reading_chunk(2, 1)
    assert diary_entry.reading_chunk(2, 1) == "three four"


"""
WHen I initialise with a five word contents
then the third call should return final partial chunk 
"""
def test_readable_chunk_third_chunk():
    diary_entry = DiaryEntry("My title", "one two three four five")
    diary_entry.reading_chunk(2, 1)
    diary_entry.reading_chunk(2, 1)
    assert diary_entry.reading_chunk(2, 1) == "five"

"""
When I initializse with five word contents
Then on the fourth call, the method should start again from the beggining 
"""

def test_readable_chunk_forth_chunk():
    diary_entry = DiaryEntry("My title", "one two three four five")
    diary_entry.reading_chunk(2, 1)
    diary_entry.reading_chunk(2, 1)
    diary_entry.reading_chunk(2, 1)
    assert diary_entry.reading_chunk(2, 1) == "one two"
