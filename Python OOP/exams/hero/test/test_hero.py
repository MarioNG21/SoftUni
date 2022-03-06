from unittest import TestCase, main

from project.hero import Hero


class HeroTest(TestCase):
    def test_hero_initialization(self):
        hero = Hero('Username', 10, 100, 75)
        self.assertEqual('Username', hero.username)
        self.assertEqual(100, hero.health)
        self.assertEqual(10, hero.level)
        self.assertEqual(75, hero.damage)

    def test_hero_str_should_return_proper_string(self):
        hero = Hero('Username', 10, 100, 75)
        expected = f"Hero {hero.username}: {hero.level} lvl\n" \
                   f"Health: {hero.health}\n" \
                   f"Damage: {hero.damage}\n"

        actual = str(hero)
        self.assertEqual(expected, actual)

    def test_hero_to_raise_exception_when_tries_to_attack_himself(self):
        hero = Hero('Username', 10, 100, 75)
        with self.assertRaises(Exception) as ex:
            hero.battle(hero)

        self.assertEqual('You cannot fight yourself', str(ex.exception))

    def test_hero_to_raise_exception_when_tries_to_attack_enemy_with_heros_name(self):
        hero = Hero('Username', 10, 100, 75)
        enemy = Hero(hero.username, 50, 100, 65)
        with self.assertRaises(Exception) as ex:
            hero.battle(enemy)

        self.assertEqual('You cannot fight yourself', str(ex.exception))

    def test_hero_to_raise_exception_when_tries_to_battle_with_negative_health(self):
        hero = Hero("Username", 10, 0, 75)
        enemy = Hero('pehso', 50, 100, 65)
        with self.assertRaises(ValueError) as ex:
            hero.battle(enemy)

        self.assertEqual('Your health is lower than or equal to 0. You need to rest', str(ex.exception))

    def test_hero_to_raise_exception_when_tries_to_battle_with_enemy_with_negative_health(self):
        hero = Hero('Username', 10, 100, 75)
        enemy = Hero("Pesho", 50, -10, 65)

        with self.assertRaises(ValueError) as ex:
            hero.battle(enemy)

        self.assertEqual(f'You cannot fight {enemy.username}. He needs to rest', str(ex.exception))

    def test_hero_to_make_draw_when_attacks_enemy(self):
        hero = Hero('Username', 10, 100, 75)
        enemy = Hero("Pesho", 10, 100, 75)

        enemy_damage = enemy.damage * enemy.level

        expected_health = hero.health - enemy_damage

        result = hero.battle(enemy)

        self.assertEqual('Draw', result)
        self.assertEqual(expected_health, hero.health)
        self.assertEqual(expected_health, enemy.health)

    def test_battle_returns_win_when_enemy_dies(self):
        hero1_level, hero1_health, hero1_damage = 10, 100, 75
        hero2_level, hero2_health, hero2_damage = hero1_level, (hero1_damage * hero1_level) + 250, hero1_health
        hero1 = Hero("username", hero1_level, hero1_health, hero1_damage)
        hero2 = Hero("Enemy", hero2_level, hero2_health, hero2_damage)

        result = hero2.battle(hero1)
        self.assertEqual('You win', result)
        self.assertEqual(hero2_level + 1, hero2.level)
        self.assertEqual(hero2_health - hero1_level * hero1_damage + 5, hero2.health)
        self.assertEqual(hero2_damage + 5, hero2.damage)

    def test_battle_returns_win_when_enemy_wins(self):
        hero1_level, hero1_health, hero1_damage = 10, 100, 75
        hero2_level, hero2_health, hero2_damage = hero1_level, (hero1_damage * hero1_level) + 250, hero1_health
        hero1 = Hero("username", hero1_level, hero1_health, hero1_damage)
        hero2 = Hero("Enemy", hero2_level, hero2_health, hero2_damage)

        result = hero1.battle(hero2)
        self.assertEqual('You lose', result)

        self.assertEqual(hero2_level + 1, hero2.level)
        self.assertEqual(hero2_health - hero1_level * hero1_damage + 5, hero2.health)
        self.assertEqual(hero2_damage + 5, hero2.damage)

if __name__ == '__main__':
    main()
