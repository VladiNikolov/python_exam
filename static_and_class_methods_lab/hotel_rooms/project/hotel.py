class Hotel:

    def __init__(self, name):
        self.name = name
        self.rooms = []

    @property
    def guests(self):
        return sum([r.guests for r in self.rooms])

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = [r for r in self.rooms if r.number == room_number][0]
        return room.take_room(people)

    def free_room(self, room_number):
        room = [r for r in self.rooms if r.number == room_number][0]
        return room.free_room()

    def status(self):
        count_free_room = [str(r.number) for r in self.rooms if not r.is_taken]
        count_taken_room = [str(r.number) for r in self.rooms if r.is_taken]
        result = f'Hotel {self.name} has {self.guests} total guests\n'
        result += f'Free rooms: {", ".join(count_free_room)}\n'
        result += f'Taken rooms: {", ".join(count_taken_room)}'

        return result




