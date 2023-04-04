from project_bookstore.bookstore import Bookstore

from unittest import TestCase, main


class TestBookstore(TestCase):

    def setUp(self) -> None:
        self.bookstore = Bookstore(5)

    def test_initializing(self):
        self.assertEqual(5, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore._Bookstore__total_sold_books)

    def test_total_books_sold_prop(self):
        self.assertEqual(0, self.bookstore.total_sold_books)

    def test_limit_setter_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = 0
        self.assertEqual(str(ve.exception), 'Books limit of 0 is not valid')

    def test_len_returns_correct_amount(self):
        self.bookstore.receive_book('Inferno', 3)
        self.assertEqual(3, len(self.bookstore))
        self.bookstore.sell_book('Inferno', 1)
        self.assertEqual(2, len(self.bookstore))

    def test_receive_book_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book('Inferno', 6)
        self.assertEqual(str(ex.exception), 'Books limit is reached. Cannot receive more books!')

    def test_receive_book(self):
        self.bookstore.receive_book('Inferno', 1)
        result = self.bookstore.receive_book('Inferno', 3)
        self.assertEqual({'Inferno': 4}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(str(result), '4 copies of Inferno are available in the bookstore.')
        self.assertEqual(len(self.bookstore), 4)
        result2 = self.bookstore.receive_book('Inferno', 1)
        self.assertEqual(str(result2), '5 copies of Inferno are available in the bookstore.')

    def test_sell_book_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book('Inferno', 1)
        self.assertEqual(str(ex.exception), 'Book Inferno doesn\'t exist!')

    def test_sell_book_raises_exception_if_not_enough_stock(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book('Inferno', 2)
            self.bookstore.sell_book('Inferno', 4)
        self.assertEqual(str(ex.exception), 'Inferno has not enough copies to sell. Left: 2')

    def test_sell_book_valid(self):
        self.bookstore.receive_book('Inferno', 1)
        self.bookstore.receive_book('Thorn', 3)
        result = self.bookstore.sell_book('Inferno', 1)
        self.assertEqual(self.bookstore.total_sold_books, 1)
        self.assertEqual({'Inferno': 0, 'Thorn': 3}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(str(result), 'Sold 1 copies of Inferno')
        self.assertEqual(len(self.bookstore), 3)
        result2 = self.bookstore.sell_book('Thorn', 2)
        self.assertEqual(result2, 'Sold 2 copies of Thorn')
        self.assertEqual(self.bookstore.total_sold_books, 3)

    def test_str_method_returns_correct_result_no_books(self):
        actual = 'Total sold books: 0\nCurrent availability: 0'
        self.assertEqual(str(self.bookstore), actual)

    def test_str_method_returns_correct_result_with_books(self):
        self.bookstore.receive_book('Inferno', 1)
        self.bookstore.sell_book('Inferno', 1)
        self.bookstore.receive_book('Thorn', 1)
        actual = 'Total sold books: 1\nCurrent availability: 1\n' \
                 ' - Inferno: 0 copies\n' \
                 ' - Thorn: 1 copies'
        self.assertEqual(str(self.bookstore), actual)


if __name__ == '__main__':
    main()
