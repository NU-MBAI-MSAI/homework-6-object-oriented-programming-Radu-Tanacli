from city import City
from operator import attrgetter

class Pandemic:
    def __init__(self):
        self.cities = []

    def add_city(self, name):
        if any(city.name == name for city in self.cities):
            raise ValueError("City already added")
        self.cities.append(City(name))

    def edit_city(self, name, infected, recovered, deaths):
        for city in self.cities:
            if city.name == name:
                city.infected = infected
                city.recovered = recovered
                city.deaths = deaths
                return
        raise ValueError("City not in list")

    def display_city(self, name):
        for city in self.cities:
            if city.name == name:
                print(city)
                return
        print("City not in list")

    def display_all_city_stats(self, attribute):
        if attribute not in ['name', 'infected', 'recovered', 'deaths']:
            raise ValueError("Invalid attribute")
        sorted_cities = sorted(self.cities, key=attrgetter(f'_{self.__class__.__name__}__{attribute}'))
        for city in sorted_cities:
            print(city)
