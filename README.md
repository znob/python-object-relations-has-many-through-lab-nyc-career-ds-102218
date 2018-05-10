
# Python Object Relationships - Has Many Through Lab

## Introduction
In this lab we are going to work on creating a **has many through** relationship. Until this point, our relationships have been pretty straight forward. But what if we are dealing with a relationship where both classes could have many of the other class. For example, we could talk about a `Doctor` and a `Patient`. We know just about everyone has more than one doctor, or they could potentially. We have eye doctors, teeth doctors (otherwise known as dentists), general practitioners (doctor you see for regular checkups), and so on. And doctors will have more than one patient if they want to have a thriving practice. Since this is a **many to many** relationship, we have to add in a third class. Dun dun dun! Don't worry -- we'll figure this out together. 

Let's ask ourselves what doctors and patients have in common. They both are usually running late? Well yes, but it doesn't seem like that would help explain their connection. What about they both have an appointment? Let's say we have doctor Danielle and patient Patrick. Doctor Danielle **has one** appointment with a patient Patrick and patient Patrick also **has one** appointment with doctor Danielle. We can also say that this appointment **belongs to** both a the doctor and the patient. This sounds like the right connection! Pretty neat, right? Let's get started translating something like this into code.

## Objectives
* Define classes for a domain with a has many through relationship
* Define instance methods that operate on and return information about the has many through relationship 

## Defining Our Classes
In this lab, we will be working with a `Driver` class, a `Passenger` class, and a `Trip` class. The relationship between these should be such that a driver has many passengers through trips and a passenger has many drivers through trips. A trip belongs to one driver and belongs to one passenger. 
* a driver should have a `name` and a `driving_style` (i.e. "nascar-like", "safe", "nyc-taxi-driver", etc.) attribute, which should both have setters and getters
* a passenger should have a `name` and an `age`
* a trip should have a `driver`, a `passenger`, a class variable `_all` which points to a list of all trip instances, and a class method, `all` that returns the `_all` list


```python
from driver import Driver
daniel = Driver("Daniel", "fast and furious")
alice = Driver("Alice", "faster and furiouser")
jeff = Driver("Jeff", "defensive")
```


```python
from passenger import Passenger
jake = Passenger("Jake", 29)
anna = Passenger("Anna", 25)
katie = Passenger("Katie", 20)
```


```python
from trip import Trip
# create trip instances here using the above passenger and driver instance objects
trip_one = None
trip_two = None
trip_three = None
trip_four = None
```

## Operating On Has Many Through Relationships

Okay, so, we have our has many through relationship set up. Now let's define some instance methods that will help us find a driver's associated passengers and vice versa.

Below, find a list of instance methods along with the expected return value for each:

> **hint**: As we can see these methods seem to be quite similar. This is a great time to have a Query class and define methods that will handle these queries, so, we don't have to define the same methods in two separate classes.


```python
daniel.trips() 
# should return a list of trip instance objects of trips 
# associated with only the given driver (i.e. daniel)
```


```python
katie.trips() 
# should return a list of trip instance objects of trips 
# associated with only the given passenger (i.e. kaite)
```


```python
daniel.passengers() 
# should return a list of passenger instance objects of passengers 
# who have taken trips with the given driver (i.e. daniel)
```


```python
katie.drivers() 
# should return a list of driver instance objects of drivers 
# who have taken trips with the given passenger (i.e. katie)
```


```python
daniel.trip_count() 
# should return the number of trips completed by the given driver (i.e. daniel)
```


```python
katie.trip_count() 
# should return the number of trips taken by the given passenger (i.e. katie)
```

Great work!

## Artists, Songs, Genres

Alright, so, we got our first has many through relationship down, let's try it again. This time, we are going to switch to a fresh domain made up of Artists, Songs, and Genres. Artists create songs of all different genres. I mean have you heard the transformation of Lady Gaga's music from hits like *Poker Face* and *Bad Romance* to songs like *Joanne* and her collaboration album, *Cheek to Cheek*, with Tony Bennett? Honestly, what *can't* she do? 

The relationships between these three is such that:
* an artist **has many** songs
* an artist **has many** genres through songs
* a song **belongs to** an artist and **belongs to** a genre
* a genre **has many** songs
* a genre **has many** artists through songs

Okay, so let's define these classes and make sure that songs have a `name`, `arist`, and `genre`. Also make sure to have a class variable `_all` and an `all` method that returns the `_all` list. Genres and artists should both have a `name` as well.

Create the proper instance methods using property decorators to get and set (read and write) each attribute for an artist, song, and genre. Then create the instance methods listed below with the description of their return values:


```python
from artist import Artist
lady_gaga = Artist("Lady Gaga")
lcd_soundsystem = Artist("LCD Soundsystem")
vulfpeck = Artist("Vulfpeck")
# create as many artists as you'd like
```


```python
from genre import Genre
pop = Genre("Pop")
rock = Genre("Rock")
alt = Genre("Alternative")
indie = Genre("Indie")
folk = Genre("Folk")
country = Genre("Country")
funk = Genre("Funk")
jam = Genre("Jam")
# create as many genres as you'd like
```


```python
from song import Song
# create song instances and associate them with artists and genres from above 
# you can make up the songs if you'd like
```


```python
lady_gaga.songs() # returns a list of songs associated with the given artist (i.e. lady_gaga)
```


```python
vulfpeck.add_song(song_name, genre) 
# takes in a song name and a genre and creates a new song and associates it with the given artist and genre
# it returns the new list of songs associated with that artist (i.e. vulfpeck)
# example: vulfpeck.add_song("Wait for the moment", indie)
```


```python
lcd_soundsystem.genres() # returns a list of genres associated with teh given artist (i.e. lcd_soundsystem)
```


```python
pop.songs() # returns a list of songs associated with the given genre (i.e. pop)
```


```python
indie.artists() # returns a list of artists associated with the given genre (i.e. indie)
```

## Summary


Great work! In this lab we worked with creating and opertating on domains that have a has many through relationship.
