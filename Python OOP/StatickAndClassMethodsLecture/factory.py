class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ['bread'] + ingredients

    @classmethod
    def peperoni(cls):
        return cls(["tomato sauce", "parmesan", 'pepperoni'])


class ItalianPizza(Pizza):
    def __init__(self, ingredients):
        super().__init__(ingredients)
        self.ingredients = ["italian bread"] + ingredients

print(Pizza.peperoni().__dict__)
print(ItalianPizza.peperoni().__dict__)
