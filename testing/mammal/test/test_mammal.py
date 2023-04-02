from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self) -> None:
        self.mammal = Mammal('Test', 'Type', 'Sound')

    def test_initialization(self):
        self.assertEqual('Test', self.mammal.name)
        self.assertEqual('Type', self.mammal.type)
        self.assertEqual('Sound', self.mammal.sound)
        self.assertEqual('animals', self.mammal._Mammal__kingdom)

    def test_make_sound_returns_correct_data(self):
        result = self.mammal.make_sound()
        self.assertEqual('Test makes Sound', result)

    def test_get_kingdom_returns_correct_data(self):
        result = self.mammal.get_kingdom()
        self.assertEqual('animals', result)

    def test_info_returns_correct_data(self):
        result = self.mammal.info()
        self.assertEqual('Test is of type Type', result)


if __name__ == '__main__':
    main()
