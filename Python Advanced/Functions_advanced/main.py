def add(*args, **kwargs):
    return args, kwargs


print(add(1, 2, 3))
print(add(x=1, y=2, z=3))
print(add(x=1, z=3, y=5))
print(add(1, 2, z=5))