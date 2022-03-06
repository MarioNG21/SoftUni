# def fibonacci(n):
#     fib = [0, 1]
#     for _ in range(2, n + 1):
#         fib.append(fib[-1] + fib[-2])
#     return fib
#
#
# def fibonacci_gen():
#     x = 0
#     y = 1
#     yield x
#     yield y
#     while True:
#         x, y = y, x + y
#         yield y
#
#
# print(fibonacci(5))
from datetime import time


def increase_by_one(iterable):
    result = [x + 1 for x in iterable]
    for x in result:
        yield x


def increase_by_1(iterable):
    for x in iterable:
        yield x + 1


ll = list(range(2 ** 23))
start = time()
iter1 = increase_by_one(ll)
print(next(iter1))
end = time()
