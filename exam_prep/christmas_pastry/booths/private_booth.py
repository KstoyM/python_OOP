from christmas_pastry.booths.booth import Booth


class PrivateBooth(Booth):
    price_per_person = 3.5

    def reserve(self, number_of_people: int):
        self.price_for_reservation = self.price_per_person * number_of_people
        self.is_reserved = True