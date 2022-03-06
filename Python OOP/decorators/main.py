def log(func):
    def wrapper():
        print(f"{func.__name__} expected")
        return func()

    return wrapper()


@log
def f1():
    return 5


# equivalent to this:

def f2():
    return 5


f2 = log(f2)
print(f2)

print(f1)
