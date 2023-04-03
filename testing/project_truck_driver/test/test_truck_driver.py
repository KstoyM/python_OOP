from unittest import TestCase, main

from project_truck_driver.truck_driver import TruckDriver


class TestTruckDriver(TestCase):

    def setUp(self) -> None:
        self.test_truck = TruckDriver('Truck', 2.5)

    def test_correct_initialization(self):
        self.assertEqual('Truck', self.test_truck.name)
        self.assertEqual(2.5, self.test_truck.money_per_mile)
        self.assertIsInstance(self.test_truck.available_cargos, dict)
        self.assertEqual(self.test_truck.available_cargos, {})
        self.assertEqual(0, self.test_truck.earned_money)
        self.assertEqual(0, self.test_truck.miles)

    def test_money_setter_raises_value_error_if_given_value_less_than_zero(self):
        with self.assertRaises(ValueError) as ve:
            self.test_truck.earned_money = -10
        self.assertEqual(str(ve.exception), 'Truck went bankrupt.')

    def test_add_cargo_raises_exception_if_cargo_already_in_cargos(self):
        with self.assertRaises(Exception) as ex:
            self.test_truck.available_cargos = {'Varna': 4}
            self.test_truck.add_cargo_offer('Varna', 10)
        self.assertEqual(str(ex.exception), 'Cargo offer is already added.')

    def test_add_cargo_offer_adds_offer_to_cargos(self):
        result = self.test_truck.add_cargo_offer('Varna', 10)
        self.assertEqual({'Varna': 10}, self.test_truck.available_cargos)
        self.assertEqual(result, 'Cargo for 10 to Varna was added as an offer.')

    def test_drive_best_cargo_offer_returns_error_if_no_offers_available(self):
        result = self.test_truck.drive_best_cargo_offer()
        self.assertEqual(str(result), "There are no offers available.")

    def test_drive_best_cargo_offer_gets_the_best_offer(self):
        self.test_truck.available_cargos = {'Varna': 300, 'Sofia': 500, 'Lovech': 200}
        result = self.test_truck.drive_best_cargo_offer()
        self.assertEqual('Truck is driving 500 to Sofia.', str(result))

    def test_drive_best_cargo_raises_earned_money(self):
        self.test_truck.available_cargos = {'Varna': 300, 'Sofia': 500, 'Lovech': 200}
        self.test_truck.drive_best_cargo_offer()
        self.assertEqual(1210, self.test_truck.earned_money)

    def test_drive_best_cargo_raises_miles(self):
        self.test_truck.available_cargos = {'Varna': 300, 'Sofia': 500, 'Lovech': 200}
        self.test_truck.drive_best_cargo_offer()
        self.assertEqual(500, self.test_truck.miles)

    def test_eat_removes_money_after_250_miles(self):
        self.test_truck.earned_money = 300
        self.test_truck.eat(250)
        self.assertEqual(280, self.test_truck.earned_money)
        self.test_truck.eat(500)
        self.assertEqual(260, self.test_truck.earned_money)

    def test_sleep_removes_money_after_1000_miles(self):
        self.test_truck.earned_money = 300
        self.test_truck.sleep(1000)
        self.assertEqual(255, self.test_truck.earned_money)

    def test_pump_gas_removes_money_after_1500_miles(self):
        self.test_truck.earned_money = 800
        self.test_truck.pump_gas(1500)
        self.assertEqual(300, self.test_truck.earned_money)

    def test_repair_truck_removes_money_after_10000_miles(self):
        self.test_truck.earned_money = 8000
        self.test_truck.repair_truck(10000)
        self.assertEqual(500, self.test_truck.earned_money)

    def test_check_for_activities_checking_for_all_activities(self):
        self.test_truck.earned_money = 15000
        self.test_truck.check_for_activities(10000)
        self.assertEqual(3250, self.test_truck.earned_money)

    def test_represent_of_the_class(self):
        result = str(self.test_truck)
        self.assertEqual('Truck has 0 miles behind his back.', result)


if __name__ == '__main__':
    main()
