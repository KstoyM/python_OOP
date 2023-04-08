from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TestTennisPlayer(TestCase):

    def setUp(self) -> None:
        self.tennis_player = TennisPlayer("Ivan", 20, 10.5)
        self.other_player = TennisPlayer("Joro", 21, 15.5)

    def test_initializing(self):
        self.assertEqual("Ivan", self.tennis_player.name)
        self.assertEqual(20, self.tennis_player.age)
        self.assertEqual(10.5, self.tennis_player.points)
        self.assertEqual([], self.tennis_player.wins)

    def test_age_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player.age = 15
        self.assertEqual(str(ve.exception), "Players must be at least 18 years of age!")

    def test_name_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player.name = 'Ss'
        self.assertEqual(str(ve.exception), "Name should be more than 2 symbols!")

    def test_if_tournament_not_in_wins(self):
        self.tennis_player.add_new_win('RolandGaros')
        result = self.tennis_player.add_new_win('RolandGaros')
        self.assertEqual("RolandGaros has been already added to the list of wins!", result)

    def test_if_tournament_successfully_added(self):
        self.tennis_player.add_new_win("RolandGaros")
        self.assertEqual("RolandGaros", self.tennis_player.wins[0])
        self.assertEqual(1, len(self.tennis_player.wins))

    def test_lt_first_player_wins(self):
        result = self.tennis_player < self.other_player
        self.assertEqual("Joro is a top seeded player and he/she is better than Ivan", result)
        self.assertTrue(self.tennis_player < self.other_player)

    def test_lt_second_player_wins(self):
        self.other_player.points = 2
        result = self.tennis_player < self.other_player
        self.assertTrue(self.tennis_player < self.other_player)
        self.assertEqual(f"Ivan is a better player than Joro", result)

    def test_string_output(self):
        result = f"Tennis Player: Ivan\n" \
                 f"Age: 20\n" \
                 f"Points: 10.5\n" \
                 f"Tournaments won: "
        self.assertEqual(result, str(self.tennis_player))

        self.tennis_player.add_new_win('1')
        self.tennis_player.add_new_win('2')
        result = f"Tennis Player: Ivan\n" \
                 f"Age: 20\n" \
                 f"Points: 10.5\n" \
                 f"Tournaments won: 1, 2"
        self.assertEqual(result, str(self.tennis_player))