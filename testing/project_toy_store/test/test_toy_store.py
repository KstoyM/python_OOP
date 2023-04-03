from project_toy_store.toy_store import ToyStore

from unittest import TestCase, main


class TestToyStore(TestCase):

    def setUp(self) -> None:
        self.test_store = ToyStore()

    def test_initialization(self):
        for key in range(ord('A'), ord('G') + 1):
            self.assertIsNone(self.test_store.toy_shelf[chr(key)])

        self.assertEqual(len(self.test_store.toy_shelf), 7)

    def test_invalid_shelf_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.test_store.add_toy('M', 'some_toy')
        self.assertEqual(str(ex.exception), "Shelf doesn't exist!")

    def test_toy_already_in_shelf_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.test_store.toy_shelf['A'] = 'Dino'
            self.test_store.add_toy('A', 'Dino')
        self.assertEqual(str(ex.exception), 'Toy is already in shelf!')

    def test_shelf_is_not_empty_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.test_store.toy_shelf['A'] = 'Dino'
            self.test_store.add_toy('A', 'Car')
        self.assertEqual(str(ex.exception), "Shelf is already taken!")

    def test_add_toy_if_valid_input(self):
        result = self.test_store.add_toy('A', 'Dino')
        self.assertEqual(self.test_store.toy_shelf['A'], 'Dino')
        self.assertEqual(str(result), 'Toy:Dino placed successfully!')

    def test_remove_toy_raises_exception_if_toy_not_existing(self):
        with self.assertRaises(Exception) as ex:
            self.test_store.remove_toy('A', 'Bob')
        self.assertEqual(str(ex.exception), "Toy in that shelf doesn't exists!")

    def test_remove_toy_from_non_existing_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.test_store.remove_toy('M', 'Bob')
        self.assertEqual(str(ex.exception), 'Shelf doesn\'t exist!')

    def test_remove_toy_valid(self):
        self.test_store.add_toy('A', 'Dino')
        result = self.test_store.remove_toy('A', 'Dino')
        self.assertIsNone(self.test_store.toy_shelf['A'])
        self.assertEqual(result, 'Remove toy:Dino successfully!')


if __name__ == '__main__':
    main()
