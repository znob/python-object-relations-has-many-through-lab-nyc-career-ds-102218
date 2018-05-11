# import Query class here
from query import Query

class Passenger:

    def __init__(self, name, age):
        self._name = name
        self._age = age

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

    def age():
        doc = "The age property."
        def fget(self):
            return self._age
        def fset(self, value):
            self._age = value
        def fdel(self):
            del self._age
        return locals()
    age = property(**age())

    def trips(self):
        trips = Query.get_trips(self)
        return trips

    def drivers(self):
        drivers = Query.get_attributes(self.trips(), "driver")
        return drivers

    def trip_count(self):
        return len(self.trips())
