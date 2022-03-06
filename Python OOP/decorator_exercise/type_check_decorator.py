def type_check(type):
    def decorator(func):
        def wrapper(*args):
            if isinstance(*args, type):
                result = func(*args)
                return result
            else:
                return 'Bad Type'
        return wrapper

    return decorator

