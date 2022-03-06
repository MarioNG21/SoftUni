from collections import deque

pizza_orders = deque([int(x) for x in input().split(', ')]) # first order
pizza_makers = [int(x) for x in input().split(', ')]        # last employyee
has_failed = False
total_pizzas = 0
while pizza_orders:
    first_pizza = pizza_orders.popleft()
    if first_pizza <= 0:
        continue
    elif first_pizza > 10:
        continue
    employee = pizza_makers.pop()
    if first_pizza <= employee:
        total_pizzas += first_pizza
    elif first_pizza > employee:
        pizza = first_pizza
        pizza -= employee

        while pizza > 0 and pizza_makers:
            for people in pizza_makers[::-1]:
                pizza -= people
                pizza_makers.pop()
                if pizza < 0:
                    break
                if not pizza_makers:
                    has_failed = True
                    break
            if not has_failed:
                total_pizzas += first_pizza
        else:
            pizza_orders.appendleft(pizza)
    if not pizza_makers:
        break

if not pizza_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas}")
    print(f"Employees: {', '.join([str(x) for x in pizza_makers])}")
elif pizza_orders and not pizza_makers:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(x) for x in pizza_orders])}")