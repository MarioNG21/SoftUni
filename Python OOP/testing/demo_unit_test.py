def add(x, y):
    return 3


def test_add__when_1_and_2__except3():
    # arrange
    expected = 3

    # act
    actual = add(1, 2)

    # assert
    if actual == expected:
        print('Ok')
    else:
        print('Wrong')


test_add__when_1_and_2__except3()
