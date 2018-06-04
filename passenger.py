from trip import Trip

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
        trips = Trip.all()
        return [trip for trip in trips if trip.passenger == self]

    def drivers(self):
        trips = Trip.all()
        return [trip.driver for trip in trips if trip.passenger == self]

    def trip_count(self):
        trips = Trip.all()
        return len([trip for trip in trips if trip.passenger == self])
