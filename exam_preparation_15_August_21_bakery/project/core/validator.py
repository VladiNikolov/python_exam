class Validator:

    @staticmethod
    def raise_if_string_is_empty_or_whitespace(value: str, message: str):
        if value.strip() == "":
            raise ValueError(message)

    @staticmethod
    def raise_if_number_is_zero_or_negative(value: int, message: str):
        if value <= 0:
            raise ValueError(message)

    @staticmethod
    def raise_if_number_not_in_range(number, min_value, max_value, message):
        if number < min_value or number > max_value:
            raise ValueError(message)