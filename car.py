class Car:

    _all = []

    def __init__(self, make, model, year):
        self._make = make
        self._model = model
        self._year = year
        #remember to associate a car with its owner
