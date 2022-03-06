from unittest import TestCase, main

from project.train.train import Train


class TestTrain(TestCase):
    def setUp(self):
        self.train = Train('pesho', 2)

    def test_class_attr(self):
        self.assertEqual("Train is full", self.train.TRAIN_FULL)
        self.assertEqual("Passenger {} Exists", self.train.PASSENGER_EXISTS)
        self.assertEqual("Passenger Not Found", self.train.PASSENGER_NOT_FOUND)
        self.assertEqual("Added passenger {}", self.train.PASSENGER_ADD)
        self.assertEqual("Removed {}", self.train.PASSENGER_REMOVED)
        self.assertEqual(0, self.train.ZERO_CAPACITY)

    def test_train_initilization(self):
        self.assertEqual('pesho', self.train.name)
        self.assertEqual(2, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add_method_when_full_capacity_should_raise_Exception(self):
        self.train.add('Gosho')
        self.train.add('sahsko')
        with self.assertRaises(ValueError) as ex:
            self.train.add("mario")

        self.assertEqual("Train is full", str(ex.exception))

    def test_add_method_when_passenger_name_does_not_exist_and_when_capacity_is_not_full_should_return_message(self):
        self.assertEqual([], self.train.passengers)
        new_passenger = 'Gosho'
        expected_message = f"Added passenger {new_passenger}"
        result = self.train.add(new_passenger)
        self.assertEqual([new_passenger], self.train.passengers)
        self.assertEqual(expected_message, result)

    def test_add_method_when_name_already_is_registered_should_raise_Exception(self):
        passenger_name = "gosho"
        self.train.add(passenger_name)
        expected_error_message = f"Passenger {passenger_name} Exists"
        with self.assertRaises(ValueError) as ex:
            self.train.add(passenger_name)

        self.assertEqual(expected_error_message, str(ex.exception))

    def test_remove_method_if_name_doest_not_exist_should_raise_Exception(self):
        passenger_name = "Mario"
        expected_error_message = "Passenger Not Found"
        with self.assertRaises(ValueError) as ex:
            self.train.remove(passenger_name)

        self.assertEqual(expected_error_message, str(ex.exception))

    def test_remove_method_when_name_is_already_in_passenger_list_should_remove_it(self):
        passenger_name = "Mario"
        expected_message = f"Removed {passenger_name}"
        self.train.add(passenger_name)
        self.assertEqual([passenger_name], self.train.passengers)
        result = self.train.remove(passenger_name)
        self.assertEqual([], self.train.passengers)
        self.assertEqual(expected_message, result)



if __name__ == '__main__':
    main()
