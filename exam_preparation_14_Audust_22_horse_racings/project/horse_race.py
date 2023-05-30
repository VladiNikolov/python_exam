from project.core.validator import Validator


class HorseRace:

    RACE_TYPES = [
        "Winter",
        "Spring",
        "Autumn",
        "Summer"
    ]

    def __init__(self, race_type: str):
        self.race_type = race_type
        self.jockeys = []

    @property
    def race_type(self):
        return self.__race_type

    @race_type.setter
    def race_type(self, value):
        if value not in HorseRace.RACE_TYPES:
            raise ValueError("Race type does not exist!")
        self.__race_type = value

        Validator.raise_if_race_type_is_not_valid(value, "Race type does not exist!")
        self.__race_type = value

