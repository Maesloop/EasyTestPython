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
            
    def test_invalid_price(self):
        with self.assertRaises(ValueError):
            self.cart.add_item("hruška", -5)
    def test_update_price(self):
        self.cart.add_item("jablko", 30, 5)
        self.assertTrue(self.cart.update_item_price("jablko",20))
    def test_clear_cart(self):
        self.cart.add_item("jablko", 20,5)
        self.cart.clear_cart()
        self.assertEqual(self.cart.clear_cart(), True)
    def test_get_item_counts(self):
        self.cart.add_item("jablko", 20,2)
        self.cart.add_item("hruska", 20,5)
        self.assertEqual(self.cart.get_item_count(),7)
        print(self.cart.get_item_count())
    def test_cart_contents(self):
        self.cart.add_item("jablko", 20,2)
        self.cart.add_item("hruska", 20,3)
        print(self.cart.get_cart_contents())
        expected = ['jablko: 2 ks × 20 Kč', 'hruska: 3 ks × 20 Kč']
        self.assertEqual(self.cart.get_cart_contents(),expected)
    
    

if __name__ == "__main__":
    unittest.main()
    