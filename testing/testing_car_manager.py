from unittest import TestCase, main

class CarTest(TestCase):

    def setUp(self) -> None:
        self.car = Car('Vw', 'Golf', 7, 50)

    def test_initialization(self):
        self.assertEqual('Vw', self.car.make)
        self.assertEqual('Golf', self.car.model)
        self.assertEqual(7, self.car.fuel_consumption)
        self.assertEqual(50, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_empty_make_raises_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''
        self.assertEqual(str(ex.exception), "Make cannot be null or empty!")

    def test_empty_model_raises_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''
        self.assertEqual(str(ex.exception), "Model cannot be null or empty!")

    def test_negative_fuel_consumption(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0
        self.assertEqual(str(ex.exception), 'Fuel consumption cannot be zero or negative!')

    def test_negative_fuel_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0
        self.assertEqual(str(ex.exception), 'Fuel capacity cannot be zero or negative!')

    def test_negative_fuel_amount(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -5
        self.assertEqual(str(ex.exception), 'Fuel amount cannot be negative!')

    def test_refuel_with_negative_amount(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual(str(ex.exception), "Fuel amount cannot be zero or negative!")

    def test_refuel_wih_amount_lower_than_capacity(self):
        self.car.refuel(15)
        self.assertEqual(15, self.car.fuel_amount)

    def test_refuel_with_amount_greater_than_capacity(self):
        self.car.refuel(80)
        self.assertEqual(50, self.car.fuel_amount)

    def test_drive_with_less_fuel_than_necessary(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)
        self.assertEqual(str(ex.exception), "You don't have enough fuel to drive!")

    def test_drive_with_enough_fuel(self):
        self.car.fuel_amount = 50
        self.car.drive(100)
        self.assertEqual(43, self.car.fuel_amount)


if __name__ == "__main__":
    main()
