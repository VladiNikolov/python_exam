from abc import ABC, abstractmethod

from project.core.validator import Validator


class BaseRobot(ABC):
    def __init__(self, name: str, kind: str, price: float, weight: int):
        self.name = name
        self.kind = kind
        self.price = price
        self.weight = weight

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_string_is_empty_or_whit_whitespace(value, "Robot name cannot be empty!")
        self.__name = value

    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, value):
        Validator.raise_if_string_is_empty_or_whit_whitespace(value, "Robot kind cannot be empty!")
        self.__kind = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        Validator.raise_if_value_is_zero_float_or_negative(value, "Robot price cannot be less than or equal to 0.0!")
        self.__price = value

    @abstractmethod
    def eating(self):
        pass

    @property
    @abstractmethod
    def robot_type(self):
        pass

