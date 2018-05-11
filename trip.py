class Trip:

    _all = []

    def __init__(self, driver, passenger):
        self._driver = driver
        self._passenger = passenger
        Trip._all.append(self)
        # remember to keep track of all trip instances

    def driver():
        doc = "The driver property."
        def fget(self):
            return self._driver
        def fset(self, value):
            self._driver = value
        def fdel(self):
            del self._driver
        return locals()
    driver = property(**driver())

    def passenger():
        doc = "The passenger property."
        def fget(self):
            return self._passenger
        def fset(self, value):
            self._passenger = value
        def fdel(self):
            del self._passenger
        return locals()
    passenger = property(**passenger())

    @classmethod
    def all(cls):
        return cls._all
