# remeber to import the Query class here
from query import Query

class Artist:

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

    def genres(self):
        genres = Query.get_attributes(self.songs(), "genre")
        return genres
