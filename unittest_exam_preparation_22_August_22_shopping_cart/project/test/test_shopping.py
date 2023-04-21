from project.shopping_cart import ShoppingCart

from unittest import TestCase, main

class ShoppingCardTests(TestCase):

    def test_correct_init(self):
        shopping_cart = ShoppingCart("Lidl", 100)
        self.assertEqual("Lidl", shopping_cart.shop_name)
        self.assertEqual(100, shopping_cart.budget)
        self.assertEqual({}, shopping_cart.products)

    def test_correct_setter_name_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            shopping_cart = ShoppingCart("lidl100", 100)
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ve.exception))

    def test_add_to_cart_if_product_price_cost_too_much_raises(self):
        shopping_cart = ShoppingCart("Lidl", 100)
        with self.assertRaises(ValueError) as ve:
           shopping_cart.add_to_cart("Vafla", 101)
        self.assertEqual(f"Product Vafla cost too much!", str(ve.exception))

    def test_add_to_cart_product_name_whit_price(self):
        shopping_cart = ShoppingCart("Lidl", 100)
        shopping_cart.products = {
            "Bira": 5,
            "Vino": 10
        }
        result = shopping_cart.add_to_cart("Meso", 15)
        self.assertEqual(f"Meso product was successfully added to the cart!", result)
        self.assertEqual({"Bira": 5, "Vino": 10, "Meso": 15}, shopping_cart.products)

    def test_remove_product_from_shopping_cart(self):
        shopping_cart = ShoppingCart("Lidl", 100)
        shopping_cart.products = {
            "Bira": 5,
            "Vino": 10
        }
        result = shopping_cart.remove_from_cart("Bira")
        self.assertEqual(f"Product Bira was successfully removed from the cart!", result)
        self.assertEqual({"Vino": 10}, shopping_cart.products)

    def test_remove_product_if_not_exist(self):
        shopping_cart = ShoppingCart("Lidl", 100)
        shopping_cart.products = {
            "Bira": 5,
            "Vino": 10
        }
        with self.assertRaises(ValueError) as ve:
            shopping_cart.remove_from_cart("Meso")
        self.assertEqual(f"No product with name Meso in the cart!", str(ve.exception))

    def test__add__method(self):
        shopping_cart = ShoppingCart("Lidl", 100)
        shopping_cart.products = {
            "Bira": 5,
            "Vino": 10
        }

        shopping_cart1 = ShoppingCart("FF", 200)
        shopping_cart1.products = {
            "Jin": 8,
            "Rakia": 11
        }

        result = shopping_cart.shop_name + shopping_cart1.shop_name
        result_budget = shopping_cart.budget + shopping_cart1.budget

        self.assertEqual("LidlFF", result)
        self.assertEqual(300, result_budget)

    def test_buy_products_if_sum_product_is_over_budget(self):
        shopping_cart = ShoppingCart("Lidl", 100)
        shopping_cart.products = {
            "Bira": 55,
            "Vino": 50
        }
        with self.assertRaises(ValueError) as ve:
            shopping_cart.buy_products()
            sum(shopping_cart.products.values())

        self.assertEqual(f"Not enough money to buy the products! Over budget with 5.00lv!", str(ve.exception))

    def test_buy_products_if_budget_is_enough(self):
        shopping_cart = ShoppingCart("Lidl", 100)
        shopping_cart.products = {
            "Bira": 45,
            "Vino": 50
        }
        result = shopping_cart.buy_products()
        total_sum = sum(shopping_cart.products.values())
        self.assertEqual(f'Products were successfully bought! Total cost: {total_sum:.2f}lv.', result)


if __name__ == "__main__":
    main()