from typing import List

from horse_racings.horse_race import HorseRace
from horse_racings.horse_specification.appaloosa import Appaloosa
from horse_racings.horse_specification.horse import Horse
from horse_racings.horse_specification.thoroughbred import Thoroughbred
from horse_racings.jockey import Jockey


class HorseRaceApp:
    def __init__(self):
        self.horses: List[Horse] = []
        self.jockeys: List[Jockey] = []
        self.horse_races: List[HorseRace] = []

    def add_horse(self, horse_type, horse_name, horse_speed):
        if horse_type == "Appaloosa":
            horse = Appaloosa(horse_name, horse_speed)
        elif horse_type == 'Thoroughbred':
            horse = Thoroughbred(horse_name, horse_speed)
        else:
            return
        for h in self.horses:
            if h.name == horse_name:
                raise Exception(f"Horse {horse_name} has been already added!")
        else:
            self.horses.append(horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name, age):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                raise Exception(f"Jockey {jockey_name} has been already added!")
        else:
            self.jockeys.append(Jockey(jockey_name, age))
            return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type):
        for race in self.horse_races:
            if race.race_type == race_type:
                raise Exception(f"Race {race_type} has been already created!")
        else:
            self.horse_races.append(HorseRace(race_type))
            return f"Race {race_type} is created."

    def find_jockey_by_name(self, jockey_name):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                return jockey
        else:
            raise Exception(f"Jockey {jockey_name} could not be found!")

    def find_race_by_race_type(self, race_type):
        for race in self.horse_races:
            if race.race_type == race_type:
                return race
        else:
            raise Exception(f"Race {race_type} could not be found!")

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.find_jockey_by_name(jockey_name)
        for horse in self.horses[::-1]:
            if horse.__class__.__name__ == horse_type:
                if jockey.horse:
                    return f"Jockey {jockey_name} already has a horse."
                elif horse.is_taken:
                    raise Exception(f"Horse breed {horse_type} could not be found!")
                else:
                    jockey.horse = horse
                    horse.is_taken = True
                    return f"Jockey {jockey_name} will ride the horse {horse.name}."
        else:
            raise Exception(f"Horse breed {horse_type} could not be found!")

    def add_jockey_to_horse_race(self, race_type, jockey_name):
        jockey = self.find_jockey_by_name(jockey_name)
        race = self.find_race_by_race_type(race_type)

        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type):
        race = self.find_race_by_race_type(race_type)
        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = sorted(race.jockeys, key=lambda x: -x.horse.speed)[0]

        return f"The winner of the {race_type} race, with a speed of " \
               f"{winner.horse.speed}km/h is {winner.name}! Winner's horse: {winner.horse.name}."



