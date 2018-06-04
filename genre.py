# remeber to import the Query class here
from song import Song

class Genre:

    def __init__(self, name):
        self._name = name

    def name():
        doc = "The name property."
        def fget(self):
            return self._name
        def fset(self, value):
            self._name = value
        def fdel(self):
            del self._name
        return locals()
    name = property(**name())

    def songs(self):
        songs = Song.all()
        return [song for song in songs if song.genre == self]

    def artists(self):
        songs = Song.all()
        return [song.artist for song in songs if song.genre == self]
