def f(x):
    def internal_f(y):
        return x + y

    return internal_f


f1 = f(1)
print(f1)
print(f1(2))
print(f1(3))
print(f1(4))