
def shopping_list(budget: int, **kwargs):
    bought_products = []
    products_to_buy = kwargs
    result = ''
    if budget < 100:
        return 'You do not have enough budget.'
    else:
        for key, value in products_to_buy.items():
            price_for_all = value[0] * value[1]
            if price_for_all <= budget:
                if len(bought_products) < 5:
                    budget -= price_for_all
                    bought_products.append(key)
                    result += f"You bought {key} for {price_for_all:.2f} leva." + '\n'
    return result.rstrip()


print(shopping_list(100, microwave=(70, 2), skirts=(15, 4), coffee=(1.50, 10)))
print(shopping_list(20,jeans=(19.99, 1),))
print(shopping_list(104,cola=(1.20, 2),candies=(0.25, 15),bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
