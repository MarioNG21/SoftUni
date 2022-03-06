def even_parameters(func):
    def wrapper(*args):
        if all([isinstance(el, int) and el % 2 == 0 for el in args ]):
            result = func(*args)
            return result
        else:
            return 'Please use only even numbers!'
    return wrapper


@even_parameters
def add(a, b):
    return a + b

print(add("Peter", 4))