import unittest
from unittest import TestCase, main

from cat import Cat


class CatTests(TestCase):
    def setUp(self):
        self.cat = Cat("Sharo")

    def test_init_creates_all_attributes(self):
        self.assertEqual('Sharo', self.cat.name)
        self.assertFalse(self.cat.sleepy)
        self.assertFalse(self.cat.fed)
        self.assertEqual(0, self.cat.size)

    def test_cat_size_is_increased_after_eating(self):
        # Actually
        self.assertEqual(0, self.cat.size)
        self.cat.eat()
        # Assert

        self.assertEqual(1, self.cat.size)

    def test_cat_is_fed_after_eating(self):
        self.assertFalse(self.cat.fed)
        self.cat.eat()

        # Assert
        self.assertTrue(self.cat.fed)

    def test_cat_cannot_eat_if_already_fed(self):
        self.assertFalse(self.cat.fed)
        self.cat.eat()
        self.assertTrue(self.cat.fed)
        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

    def test_cat_cannot_sleep_until_it_is_fed_raises(self):
        self.assertFalse(self.cat.fed)
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_cat_is_not_sleepy_after_sleep(self):
        self.assertFalse(self.cat.sleepy)
        self.cat.eat()
        self.assertTrue(self.cat.sleepy)
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    unittest.main()
