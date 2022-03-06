import functools
from dataclasses import dataclass


def singleton(cls):
    instances = []

    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        instance = cls(*args, **kwargs)
        if instance not in instances:
            instances.append(instance)
        return instances[0]

    return wrapper


@dataclass
class Person:
    name: str
    age: int


p1 = Person('Doncho', 19)
p2 = Person('Pesho', 21)
print(p1)
