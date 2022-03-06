from project.pet_shop import PetShop
from unittest import TestCase, main


class TestPetShop(TestCase):
    def setUp(self):
        self.pet_shop = PetShop('Mario')

    def test_pet_shop_initialization(self):
        self.assertEqual('Mario', self.pet_shop.name)
        self.assertEqual({}, self.pet_shop.food)
        self.assertEqual([], self.pet_shop.pets)

    def test_add_food_method_with_negative_qnt_should_raise_Exception(self):
        expected_error = 'Quantity cannot be equal to or less than 0'
        for qnt in range(0, -10, -1):
            with self.assertRaises(ValueError) as ex:
                self.pet_shop.add_food('chips', qnt)

            self.assertEqual(expected_error, str(ex.exception))

    def test_add_food_when_food_is_not_already_added_should_return_message(self):
        food_name = 'chips'
        qnt = 20
        expected_food = {food_name: qnt}
        expected_result = f"Successfully added {qnt:.2f} grams of {food_name}."
        result = self.pet_shop.add_food(food_name, qnt)
        self.assertEqual(expected_food, self.pet_shop.food)
        self.assertEqual(expected_result, result)

    def test_add_pet_method_with_name_not_registered_in_pets_should_return_message(self):
        pet_name = "Gosho"
        pet_name2 = "Alex"
        expected_pets = [pet_name]
        expected_result = f"Successfully added {pet_name}."
        expected_result2 = f"Successfully added {pet_name2}."
        last_pets = [pet_name, pet_name2]
        result1 = self.pet_shop.add_pet(pet_name)
        self.assertEqual(expected_pets, self.pet_shop.pets)
        self.assertEqual(expected_result, result1)
        result2 = self.pet_shop.add_pet(pet_name2)
        self.assertEqual(expected_result2, result2)
        self.assertEqual(last_pets, self.pet_shop.pets)

    def test_add_pet_with_the_same_name_should_raise_exception(self):
        pet_name = "Gosho"
        expected_error = "Cannot add a pet with the same name"
        result = self.pet_shop.add_pet(pet_name)
        self.assertEqual(f"Successfully added {pet_name}.", result)
        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet(pet_name)

        self.assertEqual(expected_error, str(ex.exception))

    def test_feed_pet_method_when_pet_name_does_not_exist_should_raise_exception(self):
        pet_name = "Gosho"
        food_name = 'chips'
        with self.assertRaises(Exception) as ex:
            self.pet_shop.feed_pet(food_name, pet_name)

        self.assertEqual(f"Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_method_when_food_name_does_not_exist_should_return_message(self):
        pet_name = "Gosho"
        food_name = 'chips'
        self.pet_shop.add_pet(pet_name)
        expected_pets = [pet_name]
        expected_result = f'You do not have {food_name}'
        result = self.pet_shop.feed_pet(food_name, pet_name)
        self.assertEqual(expected_pets, self.pet_shop.pets)
        self.assertEqual(expected_result, result)

    def test_feed_pet_method_with_food_qnt_under_100_should_return_message(self):
        pet_name = "Gosho"
        food_name = 'chips'
        qnt = 99
        expected_qnt = 1000 + qnt
        self.pet_shop.add_pet(pet_name)
        self.pet_shop.add_food(food_name, qnt)
        self.assertEqual({food_name: qnt}, self.pet_shop.food)
        result = self.pet_shop.feed_pet(food_name, pet_name)
        self.assertEqual("Adding food...", result)
        self.assertEqual({food_name: expected_qnt}, self.pet_shop.food)

    def test_feed_pet_method_with_food_qnt_over_100_should_return_message(self):
        pet_name = "Gosho"
        food_name = 'chips'
        qnt = 120
        expected_qnt = qnt - 100
        expected_result = f"{pet_name} was successfully fed"
        self.pet_shop.add_pet(pet_name)
        self.pet_shop.add_food(food_name, qnt)
        self.assertEqual({food_name: qnt}, self.pet_shop.food)
        result = self.pet_shop.feed_pet(food_name, pet_name)
        self.assertEqual(expected_result, result)
        self.assertEqual({food_name: expected_qnt}, self.pet_shop.food)

    def test_repr_method(self):
        pet_name = "Gosho"
        pet_name2 = 'Alex'
        self.pet_shop.add_pet(pet_name)
        self.pet_shop.add_pet(pet_name2)
        expected_pets = [pet_name, pet_name2]
        expected_result = f'Shop {self.pet_shop.name}:\n' \
                          f'Pets: {", ".join(expected_pets)}'

        self.assertEqual(expected_result, str(self.pet_shop))


if __name__ == '__main__':
    main()
