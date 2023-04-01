class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


import unittest


class CatTests(unittest.TestCase):

    def setUp(self) -> None:
        self.tom = Cat('Tom')

    def test_initialization(self):
        self.assertEqual(self.tom.name, 'Tom')
        assert not self.tom.fed
        assert not self.tom.sleepy
        assert self.tom.size == 0

    def test_cat_size_increasing_after_eating(self):
        self.tom.eat()
        self.assertTrue(self.tom.size, 1)

    def test_cat_is_fed_after_eating(self):
        self.tom.eat()
        self.assertTrue(self.tom.fed)

    def test_cat_is_sleepy_after_eating(self):
        self.tom.eat()
        self.assertTrue(self.tom.sleepy)

    def test_cat_cannot_eat_if_already_fed(self):
        self.tom.eat()
        with self.assertRaises(Exception) as ex:
            self.tom.eat()
        self.assertEqual(str(ex.exception), "Already fed.")

    def test_cat_cannot_fall_asleep_if_not_fed(self):
        with self.assertRaises(Exception) as ex:
            self.tom.sleep()
        self.assertEqual(str(ex.exception), 'Cannot sleep while hungry')

    def test_cat_cannot_fall_asleep_if_not_sleepy(self):
        self.tom.eat()
        self.tom.sleep()
        self.assertFalse(self.tom.sleepy)


if __name__ == '__main__':
    unittest.main()
