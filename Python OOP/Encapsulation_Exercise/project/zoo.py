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

    def add_animal(self, animal: Animal, price: float):
        if self.__budget < price:
            return 'Not enough budget'
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"

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
        workers_sum = sum([x.salary for x in self.workers])

        if workers_sum > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= workers_sum
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        animals_money_for_care_sum = sum([x.money_for_care for x in self.animals])

        if animals_money_for_care_sum > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= animals_money_for_care_sum
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals" + "\n"

        result += self.__get_objects_status_by_type("Lion", self.animals)
        result += self.__get_objects_status_by_type("Tiger", self.animals)
        result += self.__get_objects_status_by_type("Cheetah", self.animals)

        return result.rstrip()

    def workers_status(self):
        result = f"You have {len(self.workers)} workers" + '\n'
        result += self.__get_objects_status_by_type("Keeper", self.workers)
        result += self.__get_objects_status_by_type("Caretaker", self.workers)
        result += self.__get_objects_status_by_type("Vet", self.workers)

        return  result.rstrip()

    def __get_objects_status_by_type(self, objects_type, objects_list):
        objects = [str(x) for x in objects_list if x.__class__.__name__ == objects_type]

        result = f"----- {len(objects)} {objects_type}s:" + '\n'

        for obj in objects:
            result += obj
            result += '\n'

        return result


