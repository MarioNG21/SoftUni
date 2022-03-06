from unittest import TestCase, main

from project.car import Car


class CarTest(TestCase):
    def setUp(self):
        self.car = Car('1948', 'SLS Mercedes', 1.25, 120)

    def test_init_creates_all_attributes(self):
        self.assertEqual(1.25, self.car.fuel_consumption)
        self.assertEqual(120, self.car.fuel_capacity)
        self.assertEqual('1948', self.car.make)
        self.assertEqual('SLS Mercedes', self.car.model)
        self.assertEqual(0, self.car.fuel_amount)

    def test_car_initialized_with_make_empty_str_or_0_should_raises_Exception(self):
        for make in ['', 0]:
            with self.assertRaises(Exception) as ex:
                self.car.make = make

            self.assertEqual('Make cannot be null or empty!', str(ex.exception))

    def test_set_make(self):
        self.car.make = "Tesla"
        self.assertEqual('Tesla', self.car.make)

    def test_set_model(self):
        self.car.model = 'BMW 4'
        self.assertEqual('BMW 4', self.car.model)

    def test_set_consumption(self):
        self.car.fuel_consumption = 20
        self.assertEqual(20 , self.car.fuel_consumption)

    def test_set_capacity(self):
        self.car.fuel_capacity = 120
        self.assertEqual(120, self.car.fuel_capacity)

    def test_car_initialized_with_model_empty_str_or_0_should_raises_Exception(self):
        for model in ['', 0]:
            with self.assertRaises(Exception) as ex:
                self.car.model = model

            self.assertEqual('Model cannot be null or empty!', str(ex.exception))

    def test_car_initialized_with_fuel_consumption_negative_or_equal_to_zero_should_raises_Exception(self):
        for consumption in range(0, -3, -1):
            with self.assertRaises(Exception) as ex:
                self.car.fuel_consumption = consumption

            self.assertEqual('Fuel consumption cannot be zero or negative!', str(ex.exception))

    def test_car_initialized_with_fuel_capacity_negative_or_equal_to_zero_should_raises_Exception(self):
        for capacity in range(0, -3, -1):
            with self.assertRaises(Exception) as ex:
                self.car.fuel_capacity = capacity

            self.assertEqual('Fuel capacity cannot be zero or negative!', str(ex.exception))

    def test_car_initialized_with_fuel_amount_negative_should_raises_Exception(self):
        for amount in range(-1, -3, -1):
            with self.assertRaises(Exception) as ex:
                self.car.fuel_amount = amount

            self.assertEqual('Fuel amount cannot be negative!', str(ex.exception))

    def test_refuel_when_fuel_is_negative_should_raises_Exception(self):
        for fuel in range(0, -3, -1):
            with self.assertRaises(Exception) as ex:
                self.car.refuel(fuel)

        self.assertEqual('Fuel amount cannot be zero or negative!', str(ex.exception))

    def test_refuel_when_fuel_is_positive_should_return_increased_amount(self):
        needed_amount_of_fuel = self.car.fuel_capacity - 1
        expected_amount_of_fuel = self.car.fuel_amount + needed_amount_of_fuel
        self.car.refuel(needed_amount_of_fuel)
        self.assertEqual(expected_amount_of_fuel, self.car.fuel_amount)

    def test_refuel_when_fuel_is_positive_and_overflow_should_return_the_original_capacity(self):
        needed_amount_of_fuel = self.car.fuel_capacity + 1
        expected_amount_of_fuel = self.car.fuel_capacity
        self.car.refuel(needed_amount_of_fuel)
        self.assertEqual(expected_amount_of_fuel, self.car.fuel_capacity)

    def test_drive_when_distance_is_bigger_than_the_fuel_amount_should_raise_Exception(self):
        self.car.refuel(self.car.fuel_capacity)
        max_distance = ((self.car.fuel_amount + 1) * 100) / self.car.fuel_consumption
        with self.assertRaises(Exception) as ex:
            self.car.drive(max_distance)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_when_distance_is_less_or_equal_to_the_fuel_amount_should_raise_Exception(self):
        self.car.refuel(self.car.fuel_capacity)
        max_distance = (self.car.fuel_amount * 100) / self.car.fuel_consumption
        self.car.drive(max_distance)
        self.assertEqual(0, self.car.fuel_amount)


if __name__ == "__main__":
    main()
