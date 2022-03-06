x = 5


def f1():
    print(f"From f1: {x}")


def f2():
    x = 6
    print(f"From f2: {x}")


def f3():
    x = 7

    def f31():
        print(f"From f31: {x}")

    def f32():
        x = 8
        print(f"From f32: {x}")

    print(f"From f3: {x}")
    f31()
    f32()


print(f"From global: {x}")
f1()
f2()
f3()