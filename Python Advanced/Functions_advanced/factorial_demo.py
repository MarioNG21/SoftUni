def factorial(n):
    print(f"Calculating {n}")
    if n == 0 or n == 1:
        return
    result = n * factorial(n - 1)
    print(f'f({n})= {result}')
    return result


factorial(10)