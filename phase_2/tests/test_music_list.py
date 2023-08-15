from lib.music_list import MusicList

"""
Given a track
#add_track adds it to the list
"""
def test_adds_a_track_to_list():
    music_list = MusicList()
    music_list.add_track("Artist one - track one")
    assert music_list.list_of_tracks() == ["Artist one - track one"]


"""
Given two tracks 
#add_track adds it to the list
"""
def test_adds_two_tracks():
    music_list = MusicList()
    music_list.add_track("Artist one - track one")
    music_list.add_track("Artist two - track two")
    assert music_list.list_of_tracks() == ["Artist one - track one", "Artist two - track two"]

"""
Given a track that is alredy in the list 
#add_track does not add it again to the list
"""
def test_add_track_does_not_dulpicate_tracks():
    music_list = MusicList()
    music_list.add_track("Artist one - track one")
    music_list.add_track("Artist two - track two")
    music_list.add_track("Artist two - track two")
    assert music_list.list_of_tracks() == ["Artist one - track one", "Artist two - track two"]