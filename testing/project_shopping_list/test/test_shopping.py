from project_shopping_list.shopping_cart import ShoppingCart
from unittest import TestCase, main


class TestShoppingCart(TestCase):

    def setUp(self) -> None:
        self.test_shop = ShoppingCart('Lidl', 35.5)

    def test_initialization(self):
        self.assertEqual('Lidl', self.test_shop.shop_name)
        self.assertEqual(35.5, self.test_shop.budget)
        self.assertEqual({}, self.test_shop.products)

    def test_name_setter_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.test_shop.shop_name = 'lidl'
        self.assertEqual(str(ve.exception), 'Shop must contain only letters and must start with capital letter!')
        with self.assertRaises(ValueError) as ve:
            self.test_shop.shop_name = 'L1dl'
        self.assertEqual(str(ve.exception), 'Shop must contain only letters and must start with capital letter!')

    def test_add_to_cart_raises_value_error_if_product_price_over_100(self):
        with self.assertRaises(ValueError) as ve:
            self.test_shop.add_to_cart('paper', 101)
        self.assertEqual(str(ve.exception), 'Product paper cost too much!')

    def test_add_to_cart_successfully_added(self):
        result = self.test_shop.add_to_cart('paper', 10)
        self.assertEqual({'paper': 10}, self.test_shop.products)
        self.assertEqual(str(result), "paper product was successfully added to the cart!")

    def test_remove_from_cart_raises_value_error_if_no_such_prod_in_cart(self):
        with self.assertRaises(ValueError) as ve:
            self.test_shop.remove_from_cart('paper')
        self.assertEqual(str(ve.exception), 'No product with name paper in the cart!')

    def test_remove_product(self):
        self.test_shop.add_to_cart('paper', 10)
        self.test_shop.add_to_cart('stone', 10)
        result = self.test_shop.remove_from_cart('paper')
        self.assertEqual({'stone': 10}, self.test_shop.products)
        self.assertEqual(str(result), 'Product paper was successfully removed from the cart!')

    def test_add_functionality(self):
        self.test_shop2 = ShoppingCart('Boy', 14.5)
        self.test_shop.add_to_cart('paper', 10)
        self.test_shop2.add_to_cart('mouse', 5)
        result = self.test_shop + self.test_shop2
        self.assertEqual(result.budget, 50)
        self.assertEqual(result.products, {'paper': 10, 'mouse': 5})
        self.assertEqual(result.shop_name, 'LidlBoy')
        self.assertIsInstance(result, ShoppingCart)

    def test_buy_products_raises_value_error_if_budget_not_sufficient(self):
        with self.assertRaises(ValueError) as ve:
            self.test_shop.add_to_cart('paper', 70)
            self.test_shop.buy_products()
        self.assertEqual(str(ve.exception), 'Not enough money to buy the products! Over budget with 34.50lv!')

    def test_buy_products(self):
        self.test_shop.add_to_cart('paper', 5)
        result = self.test_shop.buy_products()
        self.assertEqual(5, sum(self.test_shop.products.values()))
        self.assertEqual(str(result), 'Products were successfully bought! Total cost: 5.00lv.')