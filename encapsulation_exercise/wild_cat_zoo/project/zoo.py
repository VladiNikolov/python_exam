from project.animal import Animal
from project.worker import Worker


class Zoo:

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):

        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"

        if self.__budget < price:
            return "Not enough budget"

        self.__budget -= price
        self.animals.append(animal)
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        needed_sum = 0
        for worker in self.workers:
            needed_sum += worker.salary
        if self.__budget < needed_sum:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= needed_sum
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        needed_sum = 0
        for animal in self.animals:
            needed_sum += animal.money_for_care
        if self.__budget < needed_sum:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= needed_sum
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f'You have {len(self.animals)} animals\n'
        result += self.__build_animal_str("Lion")
        result += self.__build_animal_str("Tiger")
        result += self.__build_animal_str("Cheetah")

        return result

    def __build_animal_str(self, animal_type):
        filtered = []
        for animal in self.animals:
            if animal.__class__.__name__ == animal_type:
                filtered.append(animal)
        result = f'----- {len(filtered)} {animal_type}s:\n'
        for object in filtered:
            result += repr(object) + '\n'

        return result

    def workers_status(self):
        result = f'You have {len(self.workers)} workers\n'
        result += self.__build_worker_str("Keeper")
        result += self.__build_worker_str("Caretaker")
        result += self.__build_worker_str("Vet")

        return result

    def __build_worker_str(self, workers_type):
        filtered = []
        for worker in self.workers:
            if worker.__class__.__name__ == workers_type:
                filtered.append(worker)
        result = f'----- {len(filtered)} {workers_type}s:\n'
        for object in filtered:
            result += repr(object) + '\n'

        return result


