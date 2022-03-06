import functools

import key as key
import kw as kw
import value as value


def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(args, kwargs)

        prams = []
        if args:
            args_string = ', '.join(str(x) for x in args)

            prams.append(args_string)
        if kwargs:
            kwargs_string = ', '.join(f"{key} = {value}" for key, value in kwargs.items())
            prams.append(kwargs_string)

        prams_string = ', '.join(prams)
        print(f"{func.__name__} ({prams_string}) = {result}")

        return result

    return wrapper


@debug
def my_sum(x, u):
    return x + u

print(my_sum)
a = 5
