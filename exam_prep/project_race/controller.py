from typing import List

from project_race.car.car import Car
from project_race.car.muscle_car import MuscleCar
from project_race.car.sports_car import SportsCar
from project_race.driver import Driver
from project_race.race import Race


class Controller:
    VALID_CARS = {'MuscleCar': MuscleCar, 'SportsCar': SportsCar}

    def __init__(self):
        self.cars: List[Car] = []
        self.drivers: List[Driver] = []
        self.races: List[Race] = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type in self.VALID_CARS:
            if not any(filter(lambda x: x.model == model, self.cars)):
                new_car = self.VALID_CARS[car_type](model, speed_limit)
                self.cars.append(new_car)
                return f"{car_type} {model} is created."
            else:
                raise Exception(f"Car {model} is already created!")
        return

    def create_driver(self, driver_name: str):
        if not any(filter(lambda x: x.name == driver_name, self.drivers)):
            new_driver = Driver(driver_name)
            self.drivers.append(new_driver)
            return f"Driver {driver_name} is created."
        else:
            raise Exception(f"Driver {driver_name} is already created!")

    def create_race(self, race_name):
        if not any(filter(lambda x: x.name == race_name, self.races)):
            new_race = Race(race_name)
            self.races.append(new_race)
            return f"Race {race_name} is created."
        else:
            raise Exception(f"Race {race_name} is already created!")

    def find_driver_by_name(self, driver_name):
        driver = next(filter(lambda x: x.name == driver_name, self.drivers), None)
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")
        return driver

    def find_car_by_type(self, car_type):
        for car in self.cars[::-1]:
            if car.__class__.__name__ == car_type and not car.is_taken:
                return car
        else:
            raise Exception(f"Car {car_type} could not be found!")

    def find_race_by_name(self, race_name):
        race = next(filter(lambda x: x.name == race_name, self.races), None)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")
        return race

    def add_car_to_driver(self, driver_name, car_type):
        driver = self.find_driver_by_name(driver_name)
        car = self.find_car_by_type(car_type)

        if driver.car:
            old_model = driver.car.model
            car.is_taken = True
            driver.car.is_taken = False
            driver.car = car
            return f"Driver {driver_name} changed his car from {old_model} to {car.model}."
        else:
            driver.car = car
            car.is_taken = True
            return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name, driver_name):
        race = self.find_race_by_name(race_name)
        driver = self.find_driver_by_name(driver_name)
        if driver not in race.drivers:
            if driver.car:
                race.drivers.append(driver)
                return f"Driver {driver_name} added in {race_name} race."
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        return f"Driver {driver_name} is already added in {race_name} race."

    def start_race(self, race_name):
        race = self.find_race_by_name(race_name)
        if len(race.drivers) < 3:
            return f"Race {race_name} cannot start with less than 3 participants!"

        winners = [d for d in sorted(race.drivers, key=lambda x: -x.car.speed_limit)][:3]
        output = []
        for d in winners:
            d.number_of_wins += 1
            output.append(f"Driver {d.name} wins the {race_name} race with a speed of {d.car.speed_limit}.")
        return '\n'.join(output)

        # return '\n'.join(f'Driver {d.name} wins the {race_name} '
        #                  f'race with a speed of {d.car.speed_limit}.' for d in winners)


controller = Controller()
print(controller.create_driver("Peter"))
print(controller.create_car("SportsCar", "Porsche 718 Boxster", 470))
print(controller.add_car_to_driver("Peter", "SportsCar"))
print(controller.create_car("SportsCar", "Porsche 911", 580))
print(controller.add_car_to_driver("Peter", "SportsCar"))
print(controller.create_car("MuscleCar", "BMW ALPINA B7", 290))
print(controller.create_car("MuscleCar", "Mercedes-Benz AMG GLA 45", 420))
print(controller.create_driver("John"))
print(controller.create_driver("Jack"))
print(controller.create_driver("Kelly"))
print(controller.add_car_to_driver("Kelly", "MuscleCar"))
print(controller.add_car_to_driver("Jack", "MuscleCar"))
print(controller.add_car_to_driver("John", "SportsCar"))
print(controller.create_race("Christmas Top Racers"))
print(controller.add_driver_to_race("Christmas Top Racers", "John"))
print(controller.add_driver_to_race("Christmas Top Racers", "John"))
print(controller.add_driver_to_race("Christmas Top Racers", "Jack"))
print(controller.add_driver_to_race("Christmas Top Racers", "Kelly"))
print(controller.add_driver_to_race("Christmas Top Racers", "Peter"))
print(controller.start_race("Christmas Top Racers"))
[print(d.name, d.number_of_wins) for d in controller.drivers]
