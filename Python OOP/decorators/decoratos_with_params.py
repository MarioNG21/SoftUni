def repeat(count):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(count):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@repeat
def say_hi():
    print('Hello, world')


say_hi()
