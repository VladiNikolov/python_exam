class Validator:

    @staticmethod
    def raise_if_len_is_less_than(obj_value, min_len, message):
        if len(obj_value) < min_len:
            raise ValueError(message)

    @staticmethod
    def raise_if_num_not_in_range(obj_value, min_number, max_number, message):
        if obj_value < min_number or obj_value > max_number:
            raise ValueError(message)
