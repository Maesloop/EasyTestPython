from shoppingcart import *
cart = ShoppingCart()
result = cart.add_item("rohlik",100)
result2 = cart.add_item("chleba",100,2)
result3 = cart.add_item("rohlik",10,5)
cart.remove_item("rohlik",2)
print (cart.items)
cart.apply_discount("SLEVA10")
cart.get_total()
print(cart.get_total())

