import unittest2 as unittest
import sys
sys.path.insert(0, '..')
from query import Query
from driver import Driver
from trip import Trip
from passenger import Passenger

class TestOneToManyRelationships(unittest.TestCase):

    global driver_1
    driver_1 = Driver("Daniel", "fast and furious")
    global driver_2
    driver_2 = Driver("Alice", "faster and furiouser")
    global passenger_1
    passenger_1 = Passenger("Michael Scott", 38)
    global passenger_2
    passenger_2 = Passenger("Anna", 25)
    global passenger_3
    passenger_3 = Passenger("Katie", 20)
    global trip_1
    trip_1 = Trip(driver_1, passenger_1)
    global trip_2
    trip_2 = Trip(driver_1, passenger_2)
    global trip_3
    trip_3 = Trip(driver_1, passenger_3)
    global trip_4
    trip_4 = Trip(driver_2, passenger_3)
    global trip_5
    trip_5 = Trip(driver_2, passenger_2)

    def test_passenger_property_methods(self):
        self.assertEqual(passenger_1._name, "Michael Scott")
        self.assertEqual(passenger_1.name, "Michael Scott")
        self.assertEqual(passenger_1._age, 38)
        self.assertEqual(passenger_1.age, 38)

    def test_driver_property_methods(self):
        self.assertEqual(driver_1._name, "Daniel")
        self.assertEqual(driver_1.name, "Daniel")
        self.assertEqual(driver_1._driving_style, "fast and furious")
        self.assertEqual(driver_1.driving_style, "fast and furious")

    def test_trip_property_methods(self):
        self.assertEqual(trip_1._driver, driver_1)
        self.assertEqual(trip_1.driver, driver_1)
        self.assertEqual(trip_1._passenger, passenger_1)
        self.assertEqual(trip_1.passenger, passenger_1)

    def test_trip_class_method(self):
        self.assertItemsEqual(Trip._all, [trip_1, trip_2, trip_3, trip_4, trip_5])
        self.assertItemsEqual(Trip.all(), [trip_1, trip_2, trip_3, trip_4, trip_5])

    def test_driver_instance_methods(self):
        self.assertEqual(driver_1.trips(), [trip_1, trip_2, trip_3])
        self.assertEqual(driver_1.passengers(), [passenger_1, passenger_2, passenger_3])
        self.assertEqual(driver_1.trip_count(), 3)

    def test_passenger_instance_methods(self):
        self.assertEqual(passenger_2.trips(), [trip_2, trip_5])
        self.assertEqual(passenger_2.drivers(), [driver_1, driver_2])
        self.assertEqual(passenger_2.trip_count(), 2)
