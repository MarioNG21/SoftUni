import unittest
from unittest import TestCase

from demo_unit_test import add


class Person(object):
    MAX_AGE = 15
    MIN_AGE = 0
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__validate_age(value)
        self.__age = value

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_info(self):
        pass

    @classmethod
    def __validate_age(cls, value):
        if value < cls.MIN_AGE or cls.MAX_AGE < value:
            raise ValueError(f"Age must be between {cls.MIN_AGE} and {cls.MAX_AGE}")




class TestPerson(TestCase):

    def test_get_full_name__with_valid_name_and_age__expected_valid(self):
        # Arrange

        first_name = 'Test'
        last_name = 'Person'
        age = 7
        person = Person(first_name, last_name, age)

        # Act
        actual_full_name = person.get_full_name()

        # Assert
        expected_full_name =f"{first_name} {last_name}"
        self.assertEqual(expected_full_name, actual_full_name)
        pass
    def test_init__when_names_are_valid_age_is_negative__expect_value_exception(self):
        actual_age = Person(self.first_name, self.last_name, -1)
if __name__ == 'main__':
    unittest.main()