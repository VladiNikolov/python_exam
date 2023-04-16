class Validator:

    @staticmethod
    def raise_if_empty_str_ot_whitespace(value, message):
        if value.strip() == "":
            raise ValueError(message)

