import unittest2 as unittest
import sys
sys.path.insert(0, '..')
from driver import Driver
from trip import Trip
from passenger import Passenger
from artist import Artist
from song import Song
from genre import Genre

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
        self.assertItemsEqual(driver_1.trips(), [trip_1, trip_2, trip_3])
        self.assertItemsEqual(driver_1.passengers(), [passenger_1, passenger_2, passenger_3])
        self.assertEqual(driver_1.trip_count(), 3)

    def test_passenger_instance_methods(self):
        self.assertItemsEqual(passenger_2.trips(), [trip_2, trip_5])
        self.assertItemsEqual(passenger_2.drivers(), [driver_1, driver_2])
        self.assertEqual(passenger_2.trip_count(), 2)


    global artist_1
    artist_1 = Artist("Lady Gaga")
    global artist_2
    artist_2 = Artist("Vulfpeck")
    global genre_1
    genre_1 = Genre("Pop")
    global genre_2
    genre_2 = Genre("Indie")
    global genre_3
    genre_3 = Genre("Alternative")
    global song_1
    song_1 = Song("Joanne", artist_1, genre_1)
    global song_2
    song_2 = Song("Conscious Club", artist_2, genre_2)
    global song_3
    song_3 = Song("Back Pocket", artist_2, genre_1)
    global song_4
    song_4 = Song("El Chepe", artist_2, genre_3)
    global song_5
    song_5 = Song("Sinner's Prayer", artist_1, genre_3)

    def test_genre_property_methods(self):
        self.assertEqual(genre_1._name, "Pop")
        self.assertEqual(genre_1.name, "Pop")

    def test_artist_property_methods(self):
        self.assertEqual(artist_1._name, "Lady Gaga")
        self.assertEqual(artist_1.name, "Lady Gaga")

    def test_song_property_methods(self):
        self.assertEqual(song_1._name, "Joanne")
        self.assertEqual(song_1.name, "Joanne")
        self.assertEqual(song_1._artist, artist_1)
        self.assertEqual(song_1.artist, artist_1)
        self.assertEqual(song_1._genre, genre_1)
        self.assertEqual(song_1.genre, genre_1)

    def test_song_class_method(self):
        self.assertItemsEqual(Song._all, [song_1, song_2, song_3, song_4, song_5])
        self.assertItemsEqual(Song.all(), [song_1, song_2, song_3, song_4, song_5])

    def test_artist_instance_methods(self):
        self.assertItemsEqual(artist_1.songs(), [song_1, song_5])
        self.assertItemsEqual(artist_1.genres(), [genre_1, genre_3])

    def test_genre_instance_methods(self):
        self.assertItemsEqual(genre_3.songs(), [song_4, song_5])
        self.assertItemsEqual(genre_3.artists(), [artist_1, artist_2])
