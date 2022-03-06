import functools


def cache(func):
    cache_dict = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache_dict:
            cache_dict[args] = func(*args)

        return cache_dict[args]

    return wrapper


def count(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper


@count
@cache
def fibonacci(n):
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)

    #print(f"fib({n}) = {result}")
    return result


print(fibonacci(20))
print(fibonacci.call_count)