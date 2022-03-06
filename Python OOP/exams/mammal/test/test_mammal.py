from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal('Gosho', "Type", 'Sound')

    def test_mammal_initialization(self):
        # Act
        self.assertEqual('Gosho', self.mammal.name)
        self.assertEqual('Type', self.mammal.type)
        self.assertEqual('Sound', self.mammal.sound)
        self.assertEqual('animals', self.mammal._Mammal__kingdom)

    def test_make_sound_should_return_proper_str(self):
        expected = f"{self.mammal.name} makes {self.mammal.sound}"
        actual = self.mammal.make_sound()

        self.assertEqual(expected, actual)

    def test_get_kingdom_should_return_mammal_kingdom(self):
        self.assertEqual('animals', self.mammal.get_kingdom())

    def test_get_info(self):
        excepted = f"{self.mammal.name} is of type {self.mammal.type}"
        actual = self.mammal.info()

        self.assertEqual(excepted, actual)


if __name__ == '__main__':
    main()
