from lib.diary import Diary 

"""
Initially has an empty list of entries
"""

def test_initially_has_empty_list_of_entries():
    diary = Diary()
    assert diary.all() == []