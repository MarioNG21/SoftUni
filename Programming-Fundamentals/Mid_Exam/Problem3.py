price_rating_str = input().split(", ")
price_ratings_int = [int(num) for num in price_rating_str]
entry_point = int(input())

price = input()
left_side = []
right_side = []

entry = 0


left_sum_cheap = 0
left_sum_expensive = 0


right_sum_cheap = 0
right_sum_expensive = 0
for point in range(len(price_rating_str)):
    if point == entry_point:
        middle = price_ratings_int[point]
        entry = middle
        left_side = [int(num)for num in price_rating_str[:point]]
        right_side = [int(num) for num in price_rating_str[point+1:]]


def left_sum(collection_1: list, collection_2: list, point: int, command: str, sum_1: int, sum_2: int, position: str):
    if command == "cheap":
        for items in collection_1:
            if items < point:
                sum_1 += items
        for items_2 in collection_2:
            if items_2 < point:
                sum_2 += items_2
        if sum_1 >= sum_2:
            position = "Left"
            print(f"{position} - {sum_1}")
        else:
            position = "Right"
            print(f"{position} - {sum_2}")

    elif command == "expensive":
        for items in collection_1:
            if items >= point:
                sum_1 += items
        for items_2 in collection_2:
            if items_2 >= point:
                sum_2 += items_2
        if sum_1 >= sum_2:
            position = "Left"
            print(f"{position} - {sum_1}")
        else:
            position = "Right"
            print(f"{position} - {sum_2}")


left_sum(left_side, right_side, entry, price, 0, 0, "")
































