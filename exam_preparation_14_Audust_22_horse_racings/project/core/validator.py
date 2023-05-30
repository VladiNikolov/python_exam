class Validator:

    @staticmethod
    def raise_if_name_is_empty_string_or_whitespace(value, message):
        if value.strip() == "":
            raise ValueError(message)

    @staticmethod
    def raise_if_age_is_under_18(value, message):
        if value < 18:
            raise ValueError(message)

    @staticmethod
    def raise_if_speed_is_high_then_max_speed(value, max_speed,  message):
        if value > max_speed:
            raise ValueError(message)

    @staticmethod
    def raise_if_name_is_less_than_4_symbols(value, message):
        if len(value) < 4:
            raise ValueError(message)

    @staticmethod
    def raise_if_race_type_is_not_valid(value, message):

        RACE_TYPES = [
            "Winter",
            "Spring",
            "Autumn",
            "Summer"
        ]
        if value not in RACE_TYPES:
            raise ValueError(message)