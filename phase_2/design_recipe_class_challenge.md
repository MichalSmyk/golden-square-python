# Music List Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class MusicList:
 
    def add_track(self, track):
        # Parameters:
        #   track: string representing a single track
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the track to the self object
        pass # No code here yet

    def list_of_tracks(self):
        # Returns:
        #   an array with list of tracks
        # Side-effects:
        #   Throws an exception if no tracks
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a track
#add_track adds it to the list
"""
music_list = MusicList()
music_list.add_track("Artist one - track one")
music_list.list_of_tracks() # => "Artist one - track one"

"""
Given two tracks 
#add_track adds it to the list
"""
music_list = MusicList()
music_list.add_track("Artist one - track one")
music_list.add_track("Artist two - track two")
music_list.list_of_tracks() # => "Artist one - track one, Artist two - track two"

"""
Given a track that is alredy in the list 
#add_track does not add it again to the list
"""
music_list = MusicList()
music_list.add_track("Artist one - track one")
music_list.add_track("Artist two - track two")
music_list.add_track("Artist two - track two")
music_list.list_of_tracks() # => "Artist one - track one, Artist two - track two"

"""
Without any added tracks 
#list_of_tracks throws an error 
"""
music_list = MusicList()
music_list.list_of_tracks() # => "You have no tracks added!"
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

