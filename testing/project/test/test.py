from project.team import Team

from unittest import TestCase, main


class TestTeam(TestCase):

    def setUp(self) -> None:
        self.team = Team('Zerg')

    def test_initialization(self):
        self.assertEqual('Zerg', self.team.name)
        self.assertEqual({}, self.team.members)

    def test_invalid_name_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.team.name = '123 f213'
        self.assertEqual(str(ve.exception), 'Team Name can contain only letters!')

    def test_add_member_returns_string(self):
        self.assertEqual(len(self.team.members), 0)
        result = self.team.add_member(**{'Gosho': 14, 'Pesho': 21})
        self.assertEqual(str(result), 'Successfully added: Gosho, Pesho')
        self.assertEqual({'Gosho': 14, 'Pesho': 21}, self.team.members)
        result = self.team.add_member(**{'Ivan': 20})
        self.assertEqual(str(result), 'Successfully added: Ivan')
        self.assertEqual(len(self.team.members), 3)

    def test_add_members_does_not_return_message_if_nothing_to_add(self):
        self.assertEqual({}, self.team.members)
        result = self.team.add_member()
        self.assertEqual({}, self.team.members)
        self.assertEqual(str(result), 'Successfully added: ')

    def test_adding_the_same_member_does_not_add_it_again(self):
        self.team.add_member(**{'Gosho': 14})
        self.assertEqual(len(self.team.members), 1)
        self.team.add_member(**{'Gosho': 14})
        self.team.add_member(**{'Gosho': 18})
        self.assertEqual(len(self.team.members), 1)
        self.assertEqual(self.team.members, {'Gosho': 14})

    def test_remove_unexisting_member(self):
        self.assertEqual(len(self.team.members), 0)
        self.team.add_member(**{'Gosho': 14})
        self.assertEqual(len(self.team.members), 1)
        result = self.team.remove_member('Pesho')
        self.assertEqual(str(result), 'Member with name Pesho does not exist')
        self.assertEqual(len(self.team.members), 1)

    def test_remove_member(self):
        self.team.add_member(**{'Gosho': 14})
        self.team.add_member(**{'Pesho': 24})
        self.assertEqual(len(self.team.members), 2)
        result = self.team.remove_member('Pesho')
        self.assertEqual(len(self.team.members), 1)
        self.assertEqual(str(result), 'Member Pesho removed')

    def test_gt_true(self):
        other = Team('Protos')
        self.team.add_member(**{'Gosho': 15})
        self.team.add_member(**{'Gosho_v': 15})
        other.add_member(Gosho=14)
        result = self.team > other
        self.assertEqual(True, result)
        self.assertTrue(len(self.team.members) > len(other.members))

    def test_gt_false(self):
        self.second_team = Team('Protos')
        self.second_team.add_member(**{'Gosho': 15})
        self.assertFalse(self.team > self.second_team)

    def test_len(self):
        self.assertEqual(0, len(self.team))
        self.team.add_member(**{'Ivan': 20})
        self.assertEqual(1, len(self.team))
        self.team.add_member(**{'Pesho': 20})
        self.assertEqual(2, len(self.team))
        self.team.remove_member('Ivan')
        self.assertEqual(1, len(self.team))
        self.assertEqual({'Pesho': 20}, self.team.members)
        self.team.add_member(**{'Pesho': 20, 'Joro': 15})
        self.assertEqual(2, len(self.team))

    def test_add(self):
        self.second_team = Team('Protos')
        self.team.add_member(**{'Ivan': 20})
        self.second_team.add_member(**{'Pesho': 21})
        new_team = self.team + self.second_team
        self.assertEqual(new_team.name, 'ZergProtos')
        self.assertEqual(new_team.members, {'Ivan': 20, 'Pesho': 21})
        self.assertEqual(len(new_team), 2)
        self.assertIsInstance(new_team, Team)

    def test_str(self):
        self.team.add_member(**{'Gosho': 14})
        self.team.add_member(**{'Ivan': 14})
        self.team.add_member(**{'Pesho': 14})
        self.team.add_member(**{'Koko': 14})
        self.team.add_member(**{'Joro': 30})
        expected = 'Team name: Zerg\n' \
                   'Member: Joro - 30-years old\n' \
                   'Member: Gosho - 14-years old\n' \
                   'Member: Ivan - 14-years old\n' \
                   'Member: Koko - 14-years old\n' \
                   'Member: Pesho - 14-years old'
        self.assertEqual(expected, str(self.team))

    def test_str_two(self):
        expected = 'Team name: Zerg'
        self.assertEqual(expected, str(self.team))


if __name__ == '__main__':
    main()
