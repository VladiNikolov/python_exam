class Validator:

    @staticmethod
    def raise_if_string_is_empty_or_whitespace(value: str, message: str):
        if value.strip() == "":
            raise ValueError(message)

    @staticmethod
    def raise_if_value_is_less_than_16(value: int, message: str):
        if value < 16:
            raise ValueError(message)
