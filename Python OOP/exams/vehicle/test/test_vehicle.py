from unittest import TestCase, main

from project.vehicle import Vehicle


class VehicleTest(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(100, 520.5)

    def test_vehicle_initialization(self):
        self.assertTrue(isinstance(self.vehicle.fuel, float))
        self.assertTrue(isinstance(self.vehicle.horse_power, float))
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)
        self.assertEqual(2.25, self.vehicle.capacity)
        self.assertEqual(2.25, self.vehicle.fuel)
        self.assertEqual(520.5, self.vehicle.horse_power)

    def test_str_method_of_vehicle_should_return_str(self):
        actual = str(self.vehicle)
        excepted = f"The vehicle has {self.vehicle.horse_power} " \
                   f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"

        self.assertEqual(excepted, actual)

    def test_drive_should_raise_error_when_not_enough_fuel(self):
        max_distance = self.vehicle.fuel / self.vehicle.fuel_consumption
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(max_distance + 1)

        self.assertEqual('Not enough fuel', str(ex.exception))

    def test_drive_should_return_actual_value_for_fuel_and_should_be_decreased(self):
        max_distance = self.vehicle.fuel / self.vehicle.fuel_consumption
        self.vehicle.drive(max_distance)
        self.assertEqual(0, self.vehicle.fuel)

    def test_refuel_should_raise_error_when_capacity_of_vehicle_is_over_the_top(self):
        max_refuel = self.vehicle.fuel
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(max_refuel)

        self.assertEqual('Too much fuel', str(ex.exception))

    def test_refuel_should_return_actual_value_for_fuel_to_be_increased(self):
        distance = 5
        self.vehicle.drive(distance)

        consumed_fuel = distance * self.vehicle.DEFAULT_FUEL_CONSUMPTION
        recharge_fuel = consumed_fuel / 2
        expected_fuel = self.vehicle.fuel + recharge_fuel
        self.vehicle.refuel(recharge_fuel)
        self.assertEqual(expected_fuel, self.vehicle.fuel)

if __name__ == '__main__':
    main()
