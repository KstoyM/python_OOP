from unittest import TestCase, main

from project_truck_driver.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self) -> None:
        self.car = Vehicle(10.5, 50)

    def test_default_fuel_consumption(self):
        self.assertEqual(1.25, self.car.DEFAULT_FUEL_CONSUMPTION)

    def test_initialization(self):
        self.assertEqual(10.5, self.car.fuel)
        self.assertEqual(self.car.fuel, self.car.capacity)
        self.assertEqual(50, self.car.horse_power)
        self.assertEqual(self.car.fuel_consumption, self.car.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_raises_error_if_not_enough_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(1000)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_reduces_fuel(self):
        self.car.drive(1)
        self.assertEqual(9.25, self.car.fuel)

    def test_refuel_raises_exception_when_fueling_over_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(40)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_if_fueling_within_capacity(self):
        self.car.drive(1)
        self.car.refuel(1)
        self.assertEqual(10.25, self.car.fuel)

    def test_correct_str_output(self):
        result = str(self.car)
        self.assertEqual('The vehicle has 50 horse power with 10.5 fuel left and 1.25 fuel consumption',
                         result)


if __name__ == '__main__':
    main()