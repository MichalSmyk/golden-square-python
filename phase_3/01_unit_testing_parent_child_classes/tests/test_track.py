from lib.track import Track
"""
GIven a title and artist
And a search keyword for the full title
Matches is true
"""

def test_matches_on_full_title():
    track = Track("Cat", "Dog")
    assert track.matches("Cat") == True