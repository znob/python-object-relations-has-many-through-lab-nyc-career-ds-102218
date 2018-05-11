# remeber to import the Query class here
from query import Query

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
        songs = Query.get_songs(self)
        return songs

    def artists(self):
        artists = Query.get_attributes(self.songs(), "artist")
        return artists
