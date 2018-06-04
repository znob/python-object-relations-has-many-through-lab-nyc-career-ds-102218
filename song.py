class Song:

    _all = []

    def __init__(self, name, artist, genre):
        self._name = name
        self._artist = artist
        self._genre = genre
        # remember to keep track of all trip instances
        Song._all.append(self)

    @classmethod
    def all(cls):
        return cls._all

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

    def artist():
        doc = "The artist property."
        def fget(self):
            return self._artist
        def fset(self, value):
            self._artist = value
        def fdel(self):
            del self._artist
        return locals()
    artist = property(**artist())

    def genre():
        doc = "The genre property."
        def fget(self):
            return self._genre
        def fset(self, value):
            self._genre = value
        def fdel(self):
            del self._genre
        return locals()
    genre = property(**genre())
