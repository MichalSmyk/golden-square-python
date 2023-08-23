from lib.music_library import MusicLibrary
from lib.track import Track

"""
When I add multiple tracks 
They are reflected in the tracks list
"""

def test_adds_and_lists_multiple_tracks():
    library = MusicLibrary()
    track_1 = Track("My Title 1", "My Artist 1")
    track_2 = Track("My Title 2", "My Artist 2")
    library.add(track_1)
    library.add(track_2)
    assert library.tracks == [track_1, track_2]