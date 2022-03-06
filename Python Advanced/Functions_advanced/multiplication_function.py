def multiply(*args):
    if not args:
        return None
    result = 1
    for el in args:
        result *= el
    return result


print(multiply(2, 0, 1000, 5000))
