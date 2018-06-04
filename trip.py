class Trip:

    _all = []

    def __init__(self, driver, passenger):
        self._driver = driver
        self._passenger = passenger
        # remember to keep track of all trip instances
