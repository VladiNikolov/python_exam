class Validator:

    @staticmethod
    def raise_if_string_is_empty(value, message):
        if value == "":
            raise ValueError(message)

    @staticmethod
    def raise_if_price_is_zero_or_negative(value, message):
        if value <= 0:
            raise ValueError(message)