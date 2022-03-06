def multiply(times):
    def decoraotor(func):
        def wrapper(num):
            result = 0
            for _ in range(times):
                result += func(num)
            return result
        return wrapper
    return decoraotor


@multiply(5)
def add_ten(number):
    return number + 10


print(add_ten(6))
