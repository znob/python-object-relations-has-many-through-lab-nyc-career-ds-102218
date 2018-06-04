# remeber to import the Query class here
from trip import Trip

class Driver:

    def __init__(self, name, driving_style):
        self._name = name
        self._driving_style = driving_style

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

    def driving_style():
        doc = "The driving_style property."
        def fget(self):
            return self._driving_style
        def fset(self, value):
            self._driving_style = value
        def fdel(self):
            del self._driving_style
        return locals()
    driving_style = property(**driving_style())


    def trips(self):
        trips = Trip.all()
        return [trip for trip in trips if trip.driver == self]

    def passengers(self):
        trips = Trip.all()
        return [trip.passenger for trip in trips if trip.driver == self]

    def trip_count(self):
        trips = Trip.all()
        return len([trip for trip in trips if trip.driver == self])
