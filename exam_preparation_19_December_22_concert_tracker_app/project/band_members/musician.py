from abc import ABC, abstractmethod

from project.core.validator import Validator


class Musician(ABC):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

        skills = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_string_is_empty_or_whitespace(value, "Musician name cannot be empty!")
        self.__name = value
        
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        Validator.raise_if_value_is_less_than_16(value, "Musicians should be at least 16 years old!")
        self.__age = value

    def learn_new_skill(self, new_skill: str):
        pass
