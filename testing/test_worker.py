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


import unittest

class WorkerTests(unittest.TestCase):

    def test_initialization(self):
        worker = Worker('Test', 1000, 10)
        self.assertEqual(worker.name, 'Test')
        self.assertEqual(worker.salary, 1000)
        self.assertEqual(worker.energy, 10)
        self.assertEqual(worker.money, 0)

    def test_rest(self):
        worker = Worker('Test', 1000, 10)
        worker.rest()
        self.assertEqual(worker.energy, 11)

    def test_work_no_energy(self):
        worker = Worker('Test', 1000, 0)
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual(str(ex.exception), 'Not enough energy.')

    def test_work_negative_energy(self):
        worker = Worker('Test', 1000, -1)
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual(str(ex.exception), 'Not enough energy.')

    def test_work_with_energy_money_increased(self):
        worker = Worker('Test', 1000, 10)
        worker.work()
        self.assertEqual(worker.money, 1000)

    def test_work_with_energy_energy_decreased(self):
        worker = Worker('Test', 1000, 10)
        worker.work()
        self.assertEqual(worker.energy, 9)

    def test_get_info(self):
        worker = Worker('Test', 1000, 10)
        self.assertEqual(worker.get_info(), 'Test has saved 0 money.')


if __name__ == "__main__":
    unittest.main()
