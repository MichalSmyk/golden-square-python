from lib.music_list import MusicList

"""
Given a track
#add_track adds it to the list
"""
def test_adds_a_track_to_list():
    music_list = MusicList()
    music_list.add_track("Artist one - track one")
    assert music_list.list_of_tracks() == ["Artist one - track one"]