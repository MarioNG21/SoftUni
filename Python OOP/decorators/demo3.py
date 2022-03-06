def uppercase(func_to_be_decorated):
    def wrapper_uppercase():
        result = func_to_be_decorated()
        return str(result).upper()

    return wrapper_uppercase


def say_hi():
    return 'Hello, Mario'


say_hi = uppercase(say_hi)

print(say_hi())