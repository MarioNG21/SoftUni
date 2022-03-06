import functools


def get_even_num(func):
    @functools.wraps(func)
    def wrapper(*args):
        result = func(*args)
        return [num for num in result if num % 2 == 0]

    return wrapper


@get_even_num
def get_numbers(ll):
    return ll


print(get_numbers([1, 2, 3, 4, 5]))
