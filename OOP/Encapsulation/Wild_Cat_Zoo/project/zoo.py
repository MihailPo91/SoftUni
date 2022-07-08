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
        if self.__animal_capacity == len(self.animals):
            return "Not enough space for animal"

        if price > self.__budget:
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price
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
        total_worker_salaries = 0
        for worker in self.workers:
            total_worker_salaries += worker.salary
        if total_worker_salaries > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"
        else:
            self.__budget -= total_worker_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        total_animal_tend_cost = 0
        for animal in self.animals:
            total_animal_tend_cost += animal.money_for_care
        if total_animal_tend_cost > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."
        else:
            self.__budget -= total_animal_tend_cost
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = []
        tigers = []
        cheetahs = []
        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                lions.append(animal)
            elif animal.__class__.__name__ == "Tiger":
                tigers.append(animal)
            else:
                cheetahs.append(animal)

        result_string = f"You have {len(self.animals)} animals\n"
        result_string += f'----- {len(lions)} Lions:\n'
        for lion in lions:
            result_string += lion.__repr__() + '\n'
        result_string += f'----- {len(tigers)} Tigers:\n'
        for tiger in tigers:
            result_string += tiger.__repr__() + '\n'
        result_string += f'----- {len(cheetahs)} Cheetahs:\n'
        for cheetah in cheetahs:
            result_string += cheetah.__repr__() + '\n'

        return result_string.strip()

    def workers_status(self):
        keepers = []
        caretakers = []
        vets = []

        for worker in self.workers:
            if worker.__class__.__name__ == "Keeper":
                keepers.append(worker)
            elif worker.__class__.__name__ == "Vet":
                vets.append(worker)
            else:
                caretakers.append(worker)

        result_string = f"You have {len(self.workers)} workers\n"
        result_string += f"----- {len(keepers)} Keepers:\n"
        for keeper in keepers:
            result_string += keeper.__repr__() + '\n'
        result_string += f"----- {len(caretakers)} Caretakers:\n"
        for caretaker in caretakers:
            result_string += caretaker.__repr__() + '\n'
        result_string += f"----- {len(vets)} Vets:\n"
        for vet in vets:
            result_string += vet.__repr__() + '\n'

        return result_string.strip()


