import functools


def logged(function):
    @functools.wraps(function)
    def wrapper(*args):
        result = function(*args)
        return f"you called {function.__name__}{args}\nit returned {result}"

    return wrapper


@logged
def func(*args):
    return 3 + len(args)


# test zero
import unittest

class LoggedTests(unittest.TestCase):
    def test_zero(self):
        @logged
        def func(*args):
            return 3 + len(args)
        result = func(4, 4, 4)
        self.assertEqual(result, 'you called func(4, 4, 4)\nit returned 6')

if __name__ == '__main__':
    unittest.main()