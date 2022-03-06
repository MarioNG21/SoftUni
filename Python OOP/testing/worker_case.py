'''
•	Test if the worker is initialized with the correct name, salary, and energy
•	Test if the worker's energy is incremented after the rest method is called
•	Test if an error is raised if the worker tries to work with negative energy or equal to 0
•	Test if the worker's money is increased by his salary correctly after the work method is called
•	Test if the worker's energy is decreased after the work method is called
•	Test if the get_info method returns the proper string with correct values

'''
from unittest import TestCase

from test_worker import Worker


class TestWorker(TestCase):
    valid_name = "Worker 1"
    valid_salary = 1000
    valid_energy = 5

    def test_init__when_valid_name_salary_energy__expected_correctly_initialized(self):
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)

        self.assertEqual(self.valid_name, worker.name)
        self.assertEqual(self.valid_salary, worker.salary)
        self.assertEqual(self.valid_energy, worker.energy)

    def test_rest__when_valid__expect_energy_to_be_incremented(self):
        # Arrange
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)
        # Act
        worker.rest()
        # Assert
        self.assertEqual(self.valid_energy + 1, worker.energy)

    def test_work__when_energy_is_0__expect_to_raise(self):
        worker = Worker(self.valid_name, self.valid_salary, -1)
        with self.assertRaises(Exception):
            worker.work()

    def test_salary__when_energy_is_positive__expect_to_increase_money_by_salary_and_decrease_energy(self):
        worker = Worker(self.valid_name, self.valid_salary, self.valid_energy)
        worker.work()
        worker.work()

        self.assertEqual(self.valid_salary * 2, worker.money)
        self.assertEqual(self.valid_salary - 2, worker.energy)