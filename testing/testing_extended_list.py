from unittest import TestCase, main

# from testing.extended_list import IntegerList


class TestIntegerList(TestCase):
    def setUp(self) -> None:
        self.testlist = IntegerList('5', True, 3.5, 1, 2, 3)

    def test_initializer(self):
        self.assertEqual([1, 2, 3], self.testlist._IntegerList__data)

    def test_get_data_function(self):
        self.assertEqual([1, 2, 3], self.testlist.get_data())

    def test_add_element_raises_error_if_non_integer_is_added(self):
        with self.assertRaises(ValueError) as ve:
            self.testlist.add('row')
        self.assertEqual(str(ve.exception), 'Element is not Integer')

    def test_add_element_successfully(self):
        self.testlist.add(7)
        self.assertEqual([1, 2, 3, 7], self.testlist.get_data())

    def test_remove_index_when_equal_index_is_given(self):
        with self.assertRaises(IndexError) as ie:
            self.testlist.remove_index(3)
        self.assertEqual(str(ie.exception), 'Index is out of range')

    def test_remove_index_when_invalid_index_is_given(self):
        with self.assertRaises(IndexError) as ie:
            self.testlist.remove_index(5)
        self.assertEqual(str(ie.exception), 'Index is out of range')

    def test_remove_index_when_valid_index_is_given(self):
        self.testlist.remove_index(2)
        self.assertEqual([1, 2], self.testlist.get_data())

    def test_get_if_index_is_out_of_range(self):
        with self.assertRaises(IndexError) as ie:
            self.testlist.get(3)
        self.assertEqual(str(ie.exception), 'Index is out of range')

    def test_get_if_index_is_valid(self):
        a = self.testlist.get(2)
        self.assertEqual(a, 3)

    def test_insert_if_index_is_out_of_range(self):
        with self.assertRaises(IndexError) as ie:
            self.testlist.insert(4, 2)
        self.assertEqual(str(ie.exception), "Index is out of range")

    def test_insert_if_element_is_not_an_integer(self):
        with self.assertRaises(ValueError) as ve:
            self.testlist.insert(2, 'bool')
        self.assertEqual(str(ve.exception), "Element is not Integer")

    def test_insert_equal_with_valid_input(self):
        self.testlist.insert(2, 4)
        self.assertEqual([1, 2, 4, 3], self.testlist.get_data())

    def test_get_biggest(self):
        self.assertEqual(3, self.testlist.get_biggest())

    def test_get_index(self):
        self.assertEqual(1, self.testlist.get_index(2))


if __name__ == "__main__":
    main()
