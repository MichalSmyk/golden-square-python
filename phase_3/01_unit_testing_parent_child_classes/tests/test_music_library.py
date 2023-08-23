from lib.music_library import MusicLibrary
from unittest.mock import Mock

"""
When I add multiple tracks
And I search for a keyword
I get track that match that keyword
"""
def test_searches_by_keyword():
    library = MusicLibrary()
    fake_matching = Mock()
    fake_matching.matches.return_value = True
    library.add(fake_matching)
    fake_not_matching = Mock()
    fake_not_matching.matches.return_value = False
    library.add(fake_not_matching)
    assert library.search("hello") == [fake_matching]
