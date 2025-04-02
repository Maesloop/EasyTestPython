import unittest
from shoppingcart import ShoppingCart

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()
        
    def test_add_item(self):
        self.assertTrue(self.cart.add_item("jablko", 10, 5))
        self.assertEqual(self.cart.get_item_count(), 5)
        
    def test_invalid_item_name(self):
        with self.assertRaises(ValueError):
            self.cart.add_item("", 10)
if __name__ == "__main__":
    unittest.main()
    