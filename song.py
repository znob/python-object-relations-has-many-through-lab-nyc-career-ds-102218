class Song:

    _all = []

    def __init__(self, name, artist, genre):
        self._name = name
        self._artist = artist
        self._genre = genre
        # remember to keep track of all trip instances
