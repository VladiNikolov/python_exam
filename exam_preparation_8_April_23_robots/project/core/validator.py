class Validator:

    @staticmethod
    def raise_if_string_is_empty_or_whit_whitespace(value, message):
        if value.strip() == "":
            raise ValueError(message)

    @staticmethod
    def raise_if_value_is_zero_float_or_negative(value, message):
        if value <= 0.0:
            raise ValueError(message)

    @staticmethod
    def raise_if_value_is_zero_or_negative(value, message):
        if value <= 0:
            raise ValueError(message)