class MusicList:
    
    def __init__(self):
        self._tracks = []

    def add_track(self, track):
        if track not in self._tracks:
            self._tracks.append(track)

    def list_of_tracks(self):
       return self._tracks