from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred


class HorseFactory:

    VALID_TYPES = {
        "Appaloosa": Appaloosa,
        "Thoroughbred": Thoroughbred
    }

    def create_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type in HorseFactory.VALID_TYPES:
            return HorseFactory.VALID_TYPES[horse_type](horse_name, horse_speed)