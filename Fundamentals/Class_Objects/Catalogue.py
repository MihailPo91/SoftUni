class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        product_list = []
        for product in self.products:
            product_spelled = list(product)
            if product_spelled[0] == first_letter:
                product_list.append(product)
        return product_list

    def __repr__(self):
        self.sorted = sorted(map(str, self.products))
        return f"Items in the {self.name} catalogue:" '\n' + '\n'.join(self.sorted)


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
