
# Python Object Relationships - Has Many Through Lab
Start off with a Driver has many passengers 
then talk about okay, but also a passenger doesnt only get driven by one driver so they must also have more than one driver
this means that a driver has many passengers and a passenger has many drivers
this doesnt work because we can't decide which instance should own the responsibility of keeping track of the other
think about what these two have in common - trips
both have many trips and trips only have one passenger (in this case) and one driver 

## Introduction
In this lab we are going to work on creating a **has many through** relationship. Until this point, our relationships have been pretty straight forward. But what if we are dealing with a relationship where both classes could have many of the other class. For example, we could talk about a `Doctor` and a `Patient`. We know just about everyone has more than one doctor, or they could potentially. We have eye doctors, teeth doctors (otherwise known as dentists), general practitioners (doctor you see for regular checkups), and so on. And doctors will have more than one patient if they want to have a thriving practice. Since this is **many to many** relationship, we have to add in a third class. Dun dun dun! Don't worry -- we'll figure this out together. 

Let's ask ourselves what doctors and patients have in common. They both are usually running late? Well yes, but it doesn't seem like that would help explain their connection. What about they both have an appointment? Let's say we have doctor Danielle and patient Patrick. Doctor Danielle **has one** appointment with a patient Patrick and patient Patrick also **has one** appointment with doctor Danielle. We can also say that this appointment **belongs to** both a the doctor and the patient. This sounds like the right connection! Pretty neat, right? Let's get started translating something like this into code.

## Objectives
* ONE
* TWO 
* THREE

## Defining Our Classes
In this lab, we will be working with a `Driver` class, a `Passenger` class, and a `Trip` class. The relationship between these should be such that a driver has many passengers through trips and a passenger has many drivers through trips. A trip belongs to one driver and belongs to one passenger. 
* a driver should have a `name` and a `driving_style` attribute, which should both have setters and getters
* a passenger should have a `name` and an `age`
* a trip should have a `driver`, and a `passenger`

## Querying For Our Cars

## Summary

