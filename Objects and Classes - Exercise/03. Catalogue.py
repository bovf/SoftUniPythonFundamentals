class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []
        self.products_sorted = self.products

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, first_letter):
        return [item for item in self.products if item[0] == first_letter]

    def __repr__(self):
        self.products_sorted = sorted(self.products_sorted)
        items_alphabetically = ""
        counter = 0
        for item in self.products_sorted:
            counter += 1
            if counter == len(self.products_sorted):
                items_alphabetically += f"{item}"
            else:
                items_alphabetically += f"{item}\n"

        return f"Items in the {self.name} catalogue:\n" \
               f"{items_alphabetically}"


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
