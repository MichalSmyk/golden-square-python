from lib.track import Track
"""
GIven a title and artist
And a search keyword for the full title
Matches is true
"""

def test_matches_on_full_title():
    track = Track("Cat Title", "Dog Artist")
    assert track.matches("Cat Title") == True

"""
Given a title and an artist
And a search keyword for a partial title 
Matches is true
"""
def test_matches_on_partial_title():
    track = Track("Cat Title", "Dog Artist")
    assert track.matches("Cate") == True