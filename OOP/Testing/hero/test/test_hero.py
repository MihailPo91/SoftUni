import unittest

from project.hero import Hero


class TestHero(unittest.TestCase):
    ATTACKER_USERNAME = "Attacker"
    ATTACKER_LEVEL = 10
    ATTACKER_HEALTH = 100
    ATTACKER_DAMAGE = 75

    def setUp(self) -> None:
        self.attacker = Hero(self.ATTACKER_USERNAME, self.ATTACKER_LEVEL, self.ATTACKER_HEALTH, self.ATTACKER_DAMAGE)

    def test_hero_init(self):
        self.assertEqual(self.ATTACKER_USERNAME, self.attacker.username)
        self.assertEqual(self.ATTACKER_LEVEL, self.attacker.level)
        self.assertEqual(self.ATTACKER_HEALTH, self.attacker.health)
        self.assertEqual(self.ATTACKER_DAMAGE, self.attacker.damage)

    def test_battle__raises_when_usernames_are_equal(self):
        enemy = Hero(self.ATTACKER_USERNAME, 5, 20, 30)

        with self.assertRaises(Exception) as error:
            self.attacker.battle(enemy)

        self.assertEqual("You cannot fight yourself", str(error.exception))

    def test_battle__raises_when_attacker_health_is_below_0(self):
        enemy = Hero('Enemy', 5, 20, 30)
        self.attacker.health = 0

        with self.assertRaises(Exception) as error:
            self.attacker.battle(enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(error.exception))

    def test_battle__raises_when_enemy_health_is_below_0(self):
        enemy = Hero('Enemy', 5, 0, 30)

        with self.assertRaises(Exception) as error:
            self.attacker.battle(enemy)

        self.assertEqual(f"You cannot fight {enemy.username}. He needs to rest", str(error.exception))

    def test_battle__when_both_heroes_are_dead(self):
        enemy = Hero('Enemy', self.ATTACKER_LEVEL, self.ATTACKER_HEALTH, self.ATTACKER_DAMAGE)

        actual_result = self.attacker.battle(enemy)
        expected_result = 'Draw'
        expected_health = self.ATTACKER_HEALTH - (self.ATTACKER_LEVEL * self.ATTACKER_DAMAGE)

        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_health, self.attacker.health)
        self.assertEqual(expected_health, enemy.health)

    def test_battle__when_attacker_wins(self):
        enemy = Hero('Enemy', 1, 150, 50)

        actual_result = self.attacker.battle(enemy)
        expected_result = "You win"
        expected_level = self.ATTACKER_LEVEL + 1
        expected_health = self.ATTACKER_HEALTH - (enemy.damage * enemy.level) + 5
        expected_damage = self.ATTACKER_DAMAGE + 5
        expected_loser_health = 150 - self.ATTACKER_DAMAGE * self.ATTACKER_LEVEL

        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_level, self.attacker.level)
        self.assertEqual(expected_health, self.attacker.health)
        self.assertEqual(expected_damage, self.attacker.damage)
        self.assertEqual(expected_loser_health, enemy.health)

    def test_battle__when_enemy_wins(self):
        enemy = Hero('Enemy', 10, 1500, 50)

        actual_result = self.attacker.battle(enemy)
        expected_result = "You lose"
        expected_level = 11
        expected_health = 1500 - (self.ATTACKER_LEVEL * self.ATTACKER_DAMAGE) + 5
        expected_damage = 55
        expected_loser_health = self.ATTACKER_HEALTH - 500

        self.assertEqual(expected_result, actual_result)
        self.assertEqual(expected_level, enemy.level)
        self.assertEqual(expected_health, enemy.health)
        self.assertEqual(expected_damage, enemy.damage)
        self.assertEqual(expected_loser_health, self.attacker.health)

    def test_str__expect_to_return_correct_data(self):
        expected = f"Hero {self.ATTACKER_USERNAME}: {self.ATTACKER_LEVEL} lvl\n" \
               f"Health: {self.ATTACKER_HEALTH}\n" \
               f"Damage: {self.ATTACKER_DAMAGE}\n"
        actual = str(self.attacker)

        self.assertEqual(expected, actual)