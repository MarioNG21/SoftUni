import functools


def cache(func):
    cache_dict = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache_dict:
            cache_dict[args] = func(*args)

        return cache_dict[args]

    return wrapper()


def call_count(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)

    wrapper.call_count = 9
    return wrapper


@call_count  # decororia kolko puti se vika kasheto 
@cache
def fibonacci(n):
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
    print(f"fib({n}) = {result}")

    return result


def f(x, y, z):
    result = 0
    for i in range(x):
        result += f(x - i, y, z)
        for j in range(y):
            result += f(x, y - j, z)
            if z < 0:
                continue
            for k in range(z):
                result += f(x, y, z - k)
    print(x, y, z, result)
    return result
