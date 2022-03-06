from unittest import TestCase, main

from car_manager import Car


class CarTest(TestCase):
    def setUp(self):
        self.car = Car('1948', 'SLS Mercedes', 1.25, 120)

    def test_car_initialized_with_make_empty_str_or_0_should_raises_Exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''

        self.assertEqual('Make cannot be null or empty!', str(ex.exception))

    def test_init_creates_all_attributes(self):
        self.assertEqual(1.25, self.car.fuel_consumption)
        self.assertEqual(120, self.car.fuel_capacity)
        self.assertEqual('1945', self.car.make)
        self.assertEqual('SLS Mercedes', self.car.model)


if __name__ == "__main__":
    main()
