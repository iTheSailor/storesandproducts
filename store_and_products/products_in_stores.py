from store import Store
from products import Product


product1 = Product("Shoes", 100, "Footwear")
product2 = Product("Shirt", 50, "Clothing")
product3 = Product("Pants", 75, "Clothing")

store1 = Store("Gabe's Store")

store1.add_product(product1).add_product(product2).add_product(product3)

print(store1.name,"carries", store1.products[0].name, store1.products[1].name, store1.products[2].name, "and more!")
store1.print_products()
print()
store1.sell_product("Shoes")
print()
print("Current inventory:")
store1.print_products()
print()
store1.inflation(0.05)
print("Inflation has been applied to all products:")
store1.print_products()
print()
print("New shipment of shoes has arrived!")
product4 = Product("Shoes", 100, "Footwear")
store1.add_product(product4)
print()
print("Current inventory:")
store1.print_products()
print()
print("Clearance sale on Pants and Shirts!")
store1.set_clearance("Clothing", 0.05)
print()
print("Current inventory:")
store1.print_products()

