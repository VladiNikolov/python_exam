class Client:

    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart = []
        self.bull = 0.0
        self.ordered_quantities = {}

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        if value.isdigit() and len(value) == 10 and value[0] == "0":
            self.__phone_number = value
        else:
            raise ValueError("Invalid phone number!")


