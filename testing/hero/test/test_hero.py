from unittest import TestCase, main

from project_truck_driver.hero import Hero


class HeroTest(TestCase):

    def setUp(self) -> None:
        self.hero = Hero("Hero", 2, 10, 1)
        self.enemy = Hero('Enemy', 3, 12, 2)

    def test_initialization(self):
        self.assertEqual('Hero', self.hero.username)
        self.assertEqual(2, self.hero.level)
        self.assertEqual(10, self.hero.health)
        self.assertEqual(1, self.hero.damage)

    def test_cannot_fight_yourself_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual('You cannot fight yourself', str(ex.exception))

    def test_hero_health_below_0_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.hero.health = 0
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_enemy_health_below_0_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.enemy.health = 0
            self.hero.battle(self.enemy)
        self.assertEqual("You cannot fight Enemy. He needs to rest", str(ve.exception))

    def test_hero_and_enemy_taking_damage_while_fighting(self):
        self.hero.battle(self.enemy)
        self.assertEqual(4, self.hero.health)

    def test_enemy_taking_damage_and_increasing_stats_while_fighting(self):
        self.hero.battle(self.enemy)
        self.assertEqual(15, self.enemy.health)
        self.assertEqual(4, self.enemy.level)
        self.assertEqual(7, self.enemy.damage)

    def test_draw(self):
        self.hero.level = 6
        self.hero.damage = 2
        self.enemy.level = 5
        result = str(self.hero.battle(self.enemy))
        self.assertEqual('Draw', result)

    def test_win_and_raise_stats(self):
        self.hero.level = 6
        self.hero.damage = 2
        result = str(self.hero.battle(self.enemy))
        self.assertEqual('You win', result)
        self.assertEqual(7, self.hero.level)
        self.assertEqual(9, self.hero.health)
        self.assertEqual(7, self.hero.damage)

    def test_lose(self):
        self.enemy.damage = 10
        result = str(self.hero.battle(self.enemy))
        self.assertEqual('You lose', result)

    def test_return_output(self):
        result = str(self.hero)
        self.assertEqual('Hero Hero: 2 lvl\nHealth: 10\nDamage: 1\n', result)


if __name__ == '__main__':
    main()
