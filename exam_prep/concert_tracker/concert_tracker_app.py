from typing import List

from concert_tracker.band import Band
from concert_tracker.band_members.drummer import Drummer
from concert_tracker.band_members.guitarist import Guitarist
from concert_tracker.band_members.musician import Musician
from concert_tracker.band_members.singer import Singer
from concert_tracker.concert import Concert


class ConcertTrackerApp:
    MUSICIAN_NAMES = []
    BAND_NAMES = []

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in ["Guitarist", "Drummer", "Singer"]:
            raise ValueError("Invalid musician type!")
        if name in self.MUSICIAN_NAMES:
            raise Exception(f"{name} is already a musician!")
        if musician_type == 'Guitarist':
            curr_musician = Guitarist(name, age)
        elif musician_type == 'Drummer':
            curr_musician = Drummer(name, age)
        else:
            curr_musician = Singer(name, age)

        self.musicians.append(curr_musician)
        self.MUSICIAN_NAMES.append(name)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        if name in self.BAND_NAMES:
            raise Exception(f"{name} band is already created!")

        band = Band(name)
        self.bands.append(band)
        self.BAND_NAMES.append(name)
        return f"{name} was created."

    def create_concert(self, genre, audience, ticket_price, expenses, place):
        for concert in self.concerts:
            if concert.place == place:
                raise f"{concert.place} is already registered for {concert.genre} concert!"

        curr_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(curr_concert)
        return f"{genre} concert in {place} was added."

    def __find_musician_by_name(self, name: str):
        for musician in self.musicians:
            if musician.name == name:
                return musician
        else:
            raise Exception(f"{name} isn't a musician!")

    @staticmethod
    def __find_added_to_band_musician_by_name(band, name: str):
        for musician in band.members:
            if musician.name == name:
                return musician
        else:
            raise Exception(f"{name} isn't a member of {band.name}!")

    def __find_band_by_name(self, name: str):
        for band in self.bands:
            if band.name == name:
                return band
        else:
            raise Exception(f"{name} isn't a band!")

    def __find_concert_by_place(self, place: str):
        for concert in self.concerts:
            if concert.place == place:
                return concert

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self.__find_musician_by_name(musician_name)
        band = self.__find_band_by_name(band_name)
        band.add_member(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = self.__find_band_by_name(band_name)
        musician = self.__find_added_to_band_musician_by_name(band, musician_name)
        band.remove_member(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place, band_name):
        band = next(filter(lambda x: x.name == band_name, self.bands))
        concert = next(filter(lambda x: x.place == concert_place, self.concerts))
        for musician_type in ["Drummer", "Singer", "Guitarist"]:
            if not any(filter(lambda x: x.__class__.__name__ == musician_type, band.members)):
                raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        if concert.genre == 'Rock':
            for member in band.members:
                if member.__class__.__name__ in "Drummer" and "play the drums with drumsticks" not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif member.__class__.__name__ in "Singer" and "sing high pitch notes" not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif member.__class__.__name__ in "Guitarist" and "play rock" not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == 'Metal':
            for member in band.members:
                if member.__class__.__name__ in "Drummer" and "play the drums with drumsticks" not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif member.__class__.__name__ in "Singer" and "sing low pitch notes" not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif member.__class__.__name__ in "Guitarist" and "play metal" not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        elif concert.genre == "Jazz":
            for member in band.members:
                if member.__class__.__name__ in "Drummer" and "play the drums with drum brushes" not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif member.__class__.__name__ in "Singer" and ("sing low pitch notes" not in member.skills
                                                                or "sing high pitch notes" not in member.skills):
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")
                elif member.__class__.__name__ in "Guitarist" and "play jazz" not in member.skills:
                    raise Exception(f"The {band_name} band is not ready to play at the concert!")

        profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert_place}."
