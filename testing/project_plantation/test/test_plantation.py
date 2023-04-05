from project_plantation.plantation import Plantation

from unittest import TestCase, main


class TestPlantation(TestCase):

    def setUp(self) -> None:
        self.plantation = Plantation(10)

    def test_correct_initializing(self):
        self.assertEqual(10, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_invalid_size(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.size = -1
        self.assertEqual(str(ve.exception), 'Size must be positive number!')

    def test_hire_worker_raises_exception_if_worker_already_hired(self):
        self.plantation.hire_worker('Gosho')
        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker('Gosho')
        self.assertEqual(str(ve.exception), 'Worker already hired!')

    def test_hire_worker(self):
        result = self.plantation.hire_worker('Gosho')
        self.assertEqual(len(self.plantation.workers), 1)
        self.assertEqual('Gosho', self.plantation.workers[0])
        self.assertEqual(str(result), 'Gosho successfully hired.')

    def test_len_method(self):
        self.plantation.hire_worker('Gosho')
        self.plantation.hire_worker('Pesho')
        self.assertEqual(len(self.plantation), 0)
        self.plantation.planting('Gosho', 'roza')
        self.assertEqual(len(self.plantation), 1)
        self.plantation.planting('Gosho', 'roza')
        self.plantation.planting('Pesho', 'loze')
        self.assertEqual(len(self.plantation), 3)


    def test_planting_raises_value_error_if_no_such_worker(self):
        self.plantation.hire_worker('Gosho')
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting('Ivan', 'roza')
        self.assertEqual(str(ve.exception), 'Worker with name Ivan is not hired!')

    def test_planting_if_plantation_is_full(self):
        self.plantation.size = 1
        self.plantation.hire_worker('Gosho')
        self.plantation.planting('Gosho', 'roza')
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting('Gosho', 'weed')
        self.assertEqual(str(ve.exception), "The plantation is full!")

    def test_planing_valid(self):
        self.plantation.hire_worker('Gosho')
        self.assertEqual(len(self.plantation), 0)
        result = self.plantation.planting('Gosho', 'roza')
        self.assertEqual({'Gosho': ['roza']}, self.plantation.plants)
        self.assertEqual('roza', self.plantation.plants['Gosho'][0])
        self.assertEqual(result, 'Gosho planted it\'s first roza.')
        result_second = self.plantation.planting('Gosho', 'weed')
        self.assertEqual('weed', self.plantation.plants['Gosho'][1])
        self.assertEqual(result_second, 'Gosho planted weed.')
        self.assertEqual(len(self.plantation), 2)

    def test_str(self):
        self.plantation.hire_worker('Gosho')
        self.plantation.planting('Gosho', 'roza')

        expected = 'Plantation size: 10\n' \
                   'Gosho\n' \
                   'Gosho planted: roza'
        self.assertEqual(expected, str(self.plantation))

    def test_repr(self):
        self.plantation.hire_worker('Gosho')
        expected = 'Size: 10\n' \
                   'Workers: Gosho'
        self.assertEqual(repr(self.plantation), expected)


if __name__ == '__main__':
    main()
