class City:
    def __init__(self, name, infected=0, recovered=0, deaths=0):
        self.__name = name
        self.__infected = infected
        self.__recovered = recovered
        self.__deaths = deaths

    @property
    def name(self):
        return self.__name

    @property
    def infected(self):
        return self.__infected

    @infected.setter
    def infected(self, value):
        if value is None or not isinstance(value, int):
            raise TypeError("Infected must be an integer")
        self.__infected = value

    @property
    def recovered(self):
        return self.__recovered

    @recovered.setter
    def recovered(self, value):
        if value is None or not isinstance(value, int):
            raise TypeError("Recovered must be an integer")
        self.__recovered = value

    @property
    def deaths(self):
        return self.__deaths

    @deaths.setter
    def deaths(self, value):
        if value is None or not isinstance(value, int):
            raise TypeError("Deaths must be an integer")
        self.__deaths = value

    def __eq__(self, other):
        if isinstance(other, City):
            return self.__name == other.__name
        return False

    def __str__(self):
        return f"Name: {self.__name}\nInfected: {self.__infected}, Recovered: {self.__recovered}, Deaths: {self.__deaths}"
