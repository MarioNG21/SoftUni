from project.pet_shop import PetShop

from unittest import TestCase, main


class PetShopTest(TestCase):
    def setUp(self):
        self.pet_shop = PetShop("Friends")

    def test_pet_shop_initialization(self):
        expected_food = {}
        expected_pets = []
        self.assertEqual('Friends', self.pet_shop.name)
        self.assertEqual(expected_food, self.pet_shop.food)
        self.assertEqual(expected_pets, self.pet_shop.pets)

    def test_add_food_when_qnt_less_or_equal_to_zero_and_name_is_already_registered_should_raise_ValueError(self):
        for qnt in range(0, -3, -1):
            with self.assertRaises(ValueError) as ex:
                self.pet_shop.add_food(self.pet_shop.name, qnt)
            self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))

    def test_add_food_when_name_is_unknown_and_qnt_is_positive_should_return_zero(self):
        new_name = "Fish"
        qnt = 10.00
        expected_food = {new_name: 0 + qnt}
        result = self.pet_shop.add_food(new_name, qnt)
        self.assertIsInstance(qnt, float)
        self.assertEqual(expected_food, self.pet_shop.food)
        self.assertTrue(new_name in self.pet_shop.food)
        self.assertEqual(f"Successfully added {qnt:.2f} grams of {new_name}.", result)

    def test_add_food_when_name_is_already_set_and_qnt_is_positive(self):
        new_name = "Fish"
        qnt = 10.00
        old_result = self.pet_shop.add_food(new_name, qnt)
        self.assertIsInstance(qnt, float)
        self.assertEqual(f"Successfully added {qnt:.2f} grams of {new_name}.", old_result)
        new_qnt = 20.00
        expected_food = {new_name: qnt + new_qnt}
        result = self.pet_shop.add_food(new_name, new_qnt)
        self.assertIsInstance(new_qnt, float)
        self.assertEqual(f"Successfully added {new_qnt:.2f} grams of {new_name}.", result)
        self.assertEqual(expected_food, self.pet_shop.food)
        self.assertTrue(new_name in self.pet_shop.food)

    def test_add_pet_when_name_does_not_exist_should_return_str(self):
        pet_name = "Mario"
        expected_pets = ["Mario"]
        result = self.pet_shop.add_pet(pet_name)
        self.assertEqual(f"Successfully added {pet_name}.", result)
        self.assertEqual(expected_pets, self.pet_shop.pets)
        self.assertTrue(pet_name in self.pet_shop.pets)

    def test_add_pet_when_name_already_exist_should_return_raise_Exception(self):
        pet_name = "Mario"
        self.pet_shop.add_pet(pet_name)
        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet(pet_name)

        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_feed_pet_when_pet_name_does_not_exist_should_return_Exception(self):
        pet_name = "Mario"
        food_name = "Duner"
        self.pet_shop.add_pet('Gosho')
        with self.assertRaises(Exception) as ex:
            self.pet_shop.feed_pet(food_name, pet_name)
        self.assertEqual(f"Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_when_food_name_does_not_exist_should_return_str(self):
        pet_name = "Mario"
        self.pet_shop.add_pet(pet_name)
        self.assertTrue(pet_name in self.pet_shop.pets)
        food_name = 'Duner'
        result = self.pet_shop.feed_pet(food_name, pet_name)

        self.assertEqual(f"You do not have {food_name}", result)

    def test_feed_pet_when_the_food_qnt_is_less_than_100_should_return_str(self):
        pet_name = "Mario"
        food_name = "Duner"
        qnt = 99.99
        expected_food = {food_name: qnt}
        self.pet_shop.add_pet(pet_name)
        self.pet_shop.add_food(food_name, qnt)
        self.assertEqual(expected_food, self.pet_shop.food)
        expected_new_food = {food_name: 1000.00 + qnt}
        result = self.pet_shop.feed_pet(food_name, pet_name)
        self.assertEqual(expected_new_food, self.pet_shop.food)
        self.assertEqual("Adding food...", result)

    def test_feed_pet_when_the_food_qnt_is_larger_or_equal_to_100_should_return_str(self):
        pet_name = "Mario"
        self.pet_shop.add_pet(pet_name)
        for qnt in [100, 120]:
            food_name = "Duner"

            expected_food = {food_name: qnt}

            self.pet_shop.add_food(food_name, qnt)
            self.assertEqual(expected_food, self.pet_shop.food)
            expected_new_food = {food_name: qnt - 100}
            result = self.pet_shop.feed_pet(food_name, pet_name)
            self.assertEqual(expected_new_food, self.pet_shop.food)
            self.assertEqual(f"{pet_name} was successfully fed", result)

    def test_repr(self):

        self.pet_shop.add_pet('Gosho')
        self.pet_shop.add_pet('Mario')
        self.pet_shop.add_pet('Tigara')
        expected_pets = ['Gosho', 'Mario', 'Tigara']
        result = f'Shop {self.pet_shop.name}:\n' \
                 f'Pets: {", ".join(self.pet_shop.pets)}'
        self.assertEqual(expected_pets, self.pet_shop.pets)
        self.assertEqual(result, str(self.pet_shop))


if __name__ == '__main__':
    main()
