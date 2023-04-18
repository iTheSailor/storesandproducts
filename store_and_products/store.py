class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, new_product):
        self.products.append(new_product)
        return self

    def sell_product(self, name):
        for i in range(len(self.products)):
            if self.products[i].name == name:
                self.products.pop(i)
                print(f'Product {name} has been sold')
                return self
        return self

    def inflation(self, percent_increase):
        for i in range(len(self.products)):
            self.products[i].update_price(percent_increase, True)
        return self

    def set_clearance(self, category, percent_discount):
        for i in range(len(self.products)):
            if self.products[i].category == category:
                self.products[i].update_price(percent_discount, False)
        return self

    def print_products(self):
        for i in range(len(self.products)):
            self.products[i].print_info()
        return self