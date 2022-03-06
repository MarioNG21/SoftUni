def cache(func):
    log = {}

    def wrapper(n):
        if n in log:
            return log[n]
        result = func(n) # tuk vliza rekursiqta
        log[n] = result
        return result
    wrapper.log = log
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
                # rekusiq 1        # rekursiq 2


fibonacci(4)
print(fibonacci.log)