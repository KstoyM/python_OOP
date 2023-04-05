from project_movies.movie import Movie
from unittest import TestCase, main


class TestMovie(TestCase):

    def setUp(self) -> None:
        self.movie = Movie('Matrix', 2000, 6.5)

    def test_initializing(self):
        self.assertEqual('Matrix', self.movie.name)
        self.assertEqual(2000, self.movie.year)
        self.assertEqual(6.5, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_name_raises_value_error_if_name_is_an_empty_string(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ''
        self.assertEqual(str(ve.exception), "Name cannot be an empty string!")

    def test_year_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1500
        self.assertEqual(str(ve.exception), 'Year is not valid!')

    def test_add_actor_adds_actor(self):
        self.movie.add_actor('Neo')
        self.assertEqual(['Neo'], self.movie.actors)
        self.assertEqual(len(self.movie.actors), 1)

    def test_add_actor_returns_message(self):
        self.movie.add_actor("Neo")
        self.assertEqual(len(self.movie.actors), 1)
        result = self.movie.add_actor("Neo")
        self.assertEqual(len(self.movie.actors), 1)
        self.assertEqual(str(result), 'Neo is already added in the list of actors!')

    def test_gt_if_self_rating_higher_than_other_rating(self):
        self.second_movie = Movie('John Wick', 2010, 4)
        result = self.movie > self.second_movie
        self.assertEqual(str(result), f'"Matrix" is better than "John Wick"')

    def test_gt_if_self_rating_lower_than_other_rating(self):
        self.second_movie = Movie('John Wick', 2010, 10)
        result = self.movie > self.second_movie
        self.assertEqual(str(result), f'"John Wick" is better than "Matrix"')

    def test_repr(self):
        self.movie.add_actor('Neo')
        self.movie.add_actor('Trinity')
        expected = 'Name: Matrix\n' \
                   'Year of Release: 2000\n' \
                   'Rating: 6.50\n' \
                   'Cast: Neo, Trinity'

        self.assertEqual(expected, repr(self.movie))


if __name__ == '__main__':
    main()
