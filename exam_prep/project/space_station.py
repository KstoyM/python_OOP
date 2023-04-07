from typing import List

from project.astronaut.astronaut import Astronaut
from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    ASTRONAUT_TYPES = {'Biologist': Biologist,
                       'Geodesist': Geodesist,
                       'Meteorologist': Meteorologist}
    NUMBER_OF_SUCCESSFUL_MISSIONS = 0
    NUMBER_OF_NOT_SUCCESSFUL_MISSIONS = 0

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type: str, name: str):
        if astronaut_type in self.ASTRONAUT_TYPES:
            if not self.astronaut_repository.find_by_name(name):
                astronaut = self.ASTRONAUT_TYPES[astronaut_type](name)
                self.astronaut_repository.add(astronaut)
                return f"Successfully added {astronaut_type}: {name}."
            else:
                return f"{name} is already added."
        else:
            raise Exception("Astronaut type is not valid!")

    def add_planet(self, name, items):
        planet = self.planet_repository.find_by_name(name)
        if planet:
            return f"{name} is already added."

        new_planet = Planet(name)
        new_planet.items.extend(items.split(', '))
        self.planet_repository.add(new_planet)

        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name):
        astronaut = self.astronaut_repository.find_by_name(name)
        if astronaut:
            self.astronaut_repository.remove(astronaut)
            return f"Astronaut {astronaut.name} was retired!"
        raise Exception(f"Astronaut {name} doesn't exist!")

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name):
        if self.planet_repository.find_by_name(planet_name):
            planet = self.planet_repository.find_by_name(planet_name)
            astronauts_first = [a for a in sorted(self.astronaut_repository.astronauts, key=lambda x: -x.oxygen)]
            astronauts_for_mission = [a for a in astronauts_first if a.oxygen > 30][:5]
            if len(astronauts_for_mission) < 1:
                raise Exception("You need at least one astronaut to explore the planet!")
            for astronaut in astronauts_for_mission:

                while planet.items and astronaut.oxygen > 0:
                    astronaut.breathe()
                    astronaut.backpack.append(planet.items.pop())

            if planet.items:
                self.NUMBER_OF_NOT_SUCCESSFUL_MISSIONS += 1
                return "Mission is not completed."
            else:
                self.NUMBER_OF_SUCCESSFUL_MISSIONS += 1
                return f"Planet: {planet_name} was explored. {len([a for a in astronauts_for_mission if a.backpack])} " \
                       f"astronauts participated in collecting items."

        raise Exception("Invalid planet name!")

    def report(self):
        result = [f'{self.NUMBER_OF_SUCCESSFUL_MISSIONS} successful missions!']
        result.extend([f'{self.NUMBER_OF_NOT_SUCCESSFUL_MISSIONS} missions were not completed!'])
        result.extend(['Astronauts\' info:'])
        for a in self.astronaut_repository.astronauts:
            result.extend([f"Name: {a.name}"])
            result.extend([f"Oxygen: {a.oxygen}"])
            if a.backpack:
                result.extend([f'Backpack items: {", ".join(a.backpack)}'])
            else:
                result.extend([f'Backpack items: none'])

        return "\n".join(result)


space_station = SpaceStation()
print(space_station.add_planet('Saturn',
                               'voda, hlqb, maslo, riba, rikiq, vodka, sol, zahar'
                               ))
print(space_station.add_planet('Uran',
                               'voda, hlqb, maslo, riba, rikiq, vodka, sol, zahar'
                               ))

print(space_station.add_astronaut('Geodesist', 'Ivan'))
print(space_station.astronaut_repository.astronauts[0].oxygen)
# print(space_station.add_astronaut('Biologist', 'Ian'))
print(space_station.send_on_mission('Saturn'))
# print(space_station.send_on_mission('Uran'))
print(space_station.report())
# print(space_station.retire_astronaut('Ian'))
# print(space_station.astronaut_repository)
