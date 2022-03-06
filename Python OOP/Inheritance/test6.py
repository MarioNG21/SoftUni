from project.drink import Drink
from project.food import Food
from project.product_repository import ProductRepository

f = Food('Banana')
d = Drink('Coke')
repo = ProductRepository()
repo.add(f)
repo.add(d)
print(repo.products)