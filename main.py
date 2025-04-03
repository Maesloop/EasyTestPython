from shoppingcart import *
cart = ShoppingCart()
cart.add_item("rohlik",100,2)
cart.add_item("chleba",100,2)
cart.add_item("rohlik",100,2)
cart.remove_item("rohlik",2)
cart.apply_discount("SLEVA10")
cart.get_total()
print(cart.remove_item("maslo"))
print(cart.get_total())
print(cart.get_item_count())
print(cart.get_cart_contents())


