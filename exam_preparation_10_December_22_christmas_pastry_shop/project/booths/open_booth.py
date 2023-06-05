from project.booths.booth import Booth


class OpenBooth(Booth):
    def __init__(self, booth_number: int, capacity: int):
        super().__init__(booth_number, capacity)

    @property
    def get_price_per_person(self):
        return 2.50

    def reserve(self, number_of_people: int):
        self.price_for_reservation = number_of_people * self.get_price_per_person
        self.is_reserved = True