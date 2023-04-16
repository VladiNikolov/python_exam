from unittest import TestCase, main

from project.hero import Hero


class HeroTests(TestCase):
    def setUp(self) -> None:
        self.hero = Hero("Batman", 10, 100, 50)
        self.enemy = Hero("Robin", 10, 100, 50)

    def test_correct_init(self):
        username = "Batman"
        level = 10
        health = 100
        damage = 50

        hero = Hero(username, level, health, damage)

        self.assertEqual(username, hero.username)
        self.assertEqual(level, hero.level)
        self.assertEqual(health, hero.health)
        self.assertEqual(damage, hero.damage)

    def test_if_hero_attack_himself_rises(self):

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_if_hero_health_is_zero_rises(self):
        self.hero.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_if_hero_health_is_negative_rises(self):
        self.hero.health = -1

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_if_enemy_health_is_zero_rises(self):
        self.enemy.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(ve.exception))

    def test_if_enemy_health_is_negative_rises(self):
        self.enemy.health = -1

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(ve.exception))

    def test_battle_return_draw_when_bout_heroes_die(self):
        result = self.hero.battle(self.enemy)

        self.assertEqual("Draw", result)
        self.assertEqual(-400, self.hero.health)
        self.assertEqual(-400, self.enemy.health)

    def test_battle_hero_levels_up_after_win(self):
        enemy = Hero("Robin", 1, 100, 50)

        result = self.hero.battle(enemy)

        self.assertEqual("You win", result)
        self.assertEqual(11, self.hero.level)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(55, self.hero.damage)

    def test_battle_enemy_hero_levels_up_if_survive(self):
        hero = Hero("Batman", 1, 100, 50)
        enemy = Hero("Robin", 1, 100, 50)

        result= hero.battle(enemy)

        self.assertEqual("You lose", result)
        self.assertEqual(2, enemy.level)
        self.assertEqual(55, enemy.health)
        self.assertEqual(55, enemy.damage)

    def test_str_return_proper_string(self):
        expected_result = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
               f"Health: {self.hero.health}\n" \
               f"Damage: {self.hero.damage}\n"
        actual_result = str(self.hero)

        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    main()