import unittest


class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


from unittest import TestCase


class WorkerTest(TestCase):
    def setUp(self):
        self.worker = Worker(("Test", 100, 10))

    def test_person_is_initialized_correctly(self):
        # Arrange  -> pravim si obket] and Act

        # Assert
        self.assertEqual(self.worker.name, "Test")
        self.assertEqual(self.worker.salary, 100)
        self.assertEqual(self.worker.energy, 10)
        self.assertEqual(self.worker.money, 0)

    def test_worker_energy_increased_after_rest(self):
        # Arrange
        self.assertEqual(10, self.worker.energy)

        # Act
        self.worker.rest()
        # Assert
        self.assertEqual(11, self.worker.energy)

    def test_if_worker_can_work_with_negative_energy(self):
        # Action
        with self.assertRaises(Exception) as ex:
            self.worker.work()

        # Assertion
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_worker_money_is_increased_after_work(self):
        # Arranged

        self.assertEqual(0, self.worker.money)

        #Action
        self.worker.work()

        # Assertion
        self.assertEqual(100, self.worker.money)

    def test_worker_energy_decreased_after_work(self):
        # Arranged
        self.assertEqual(10, self.worker.energy)

        # Action
        self.worker.work()

        # Assertion
        self.assertEqual(9, self.worker.energy)

    def test_worker_get_info_method_if_it_works(self):
        # Arranged

        self.assertEqual("Test", self.worker.name)
        self.assertEqual(0, self.worker.money)

        # Act
        actual_result = self.worker.get_info()
        expected_result = 'Test has saved 0 money.'

        # Assert
        self.assertEqual(expected_result, actual_result)

if __name__ == '__main__':
    unittest.main()
