import functools


def debug(func):
    print("-- Here starts ---")

    @functools.wraps(func)
    def wrapper(*args):
    
        print(f"")
        return func(*args)

    print('-- Here ends -- ')
    return wrapper


@debug
def my_sum(x, y):
    return x + y


print(my_sum(1, 3))
