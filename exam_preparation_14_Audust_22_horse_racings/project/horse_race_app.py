from project.core.horse_factory import HorseFactory
from project.core.jockey_factory import JockeyFactory
from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:

    VALID_HORSE_TYPES = {
        "Appaloosa": Appaloosa,
        "Thoroughbred": Thoroughbred
    }

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

        self.horse_factory = HorseFactory()
        self.jockey_factory = JockeyFactory()

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):

        if horse_name in [h.name for h in self.horses]:
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type in HorseRaceApp.VALID_HORSE_TYPES:
            horse = self.VALID_HORSE_TYPES[horse_type](horse_name, horse_speed)
            self.horses.append(horse)
            return f"{horse_type} horse {horse_name} is added."

        # for horse in self.horses:
        #     if horse.name == horse_name:
        #         raise Exception(f"Horse {horse_name} has been already added!")
        #
        #     horse = self.horse_factory.create_horse(horse_type, horse_name, horse_speed)
        #     self.horses.append(horse)
        #     return f"{horse_type} horse {horse_name} is added."
        #
        #     # -> решение на Наско с допълнителен клас HorseFactory

    def add_jockey(self, jockey_name: str, age: int):
        if jockey_name in [n.name for n in self.jockeys]:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

        # for jockey in self.jockeys:
        #     if jockey.name == jockey_name:
        #         return f"Jockey {jockey_name} has been already added!"
        #
        #     jockey = self.jockey_factory.create_jockey(jockey_name, age)
        #     self.jockeys.append(jockey)
        #     return f"Jockey {jockey_name} is added."
        #
        # #     -> решение на Наско с допълнителен клас JockeyFactory

    def create_horse_race(self, race_type: str):
        if race_type in [r.race_type for r in self.horse_races]:
            raise Exception(f"Race {race_type} has been already created!")

        race = HorseRace(race_type)
        self.horse_races.append(race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        try:
            jockey = next(filter(lambda j: j.name == jockey_name, self.jockeys))
        except StopIteration:
            raise Exception(f"Jockey {jockey_name} could not be found!")
# If the jockey does NOT exist in the jockeys list raise

        try:
            horse = list(filter(lambda h: h.__class__.__name__ == horse_type and not h.is_taken, self.horses))[-1]
        except ValueError:
            raise Exception(f"Horse breed {horse_type} could not be found!")
# Sets the last horse added, from the given horse type to the jockey with the given name (if they both exist)
# If there is no available horse (all horses of that type are taken, or no horse of that type exists)

        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = horse
        horse.is_taken = True

        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        try:
            horse_race = next(filter(lambda h: h.race_type == race_type, self.horse_races))
        except StopIteration:
            raise Exception(f"Race {race_type} could not be found!")

        try:
            jockey = next(filter(lambda j: j.name == jockey_name, self.jockeys))
        except StopIteration:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in horse_race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        horse_race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."


        # horse_rase = self.__find_horse_race_by_race_type(race_type)
        # jockey = self.__find_jockey_by_name(jockey_name)
        #
        # if horse_rase is None:
        #     raise Exception(f"Race {race_type} could not be found!")
        #
        # if jockey is None:
        #     raise Exception(f"Jockey {jockey_name} could not be found!")

    def start_horse_race(self, race_type: str):
        try:
            horse_race = next(filter(lambda h: h.race_type == race_type, self.horse_races))
        except StopIteration:
            raise Exception(f"Race {race_type} could not be found!")

        if len(horse_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        highest_speed = 0
        winner = None

        for jockey in horse_race.jockeys:
            if jockey.horse.speed > highest_speed:
                highest_speed = horse_race.jockeys.speed
                winner = jockey

        return f"The winner of the {race_type} race, with a speed of {highest_speed}km/h is {winner.name}! Winner's horse: {winner.horse.name}."



    # -----------------------------------------------------------------------------------------------------------

    def __find_horse_race_by_race_type(self, race_type):
        for race in self.horse_races:
            if race.race_type == race_type:
                return race
        return None

    def __find_jockey_by_name(self, jockey_name):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                return jockey
        return None