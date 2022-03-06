def combinations(array, index):
    if len(array) == index:
        print(''.join(array))
        return
    for i in range(index, len(array)):
        array[i], array[index] = array[index], array[i]
        combinations(array, index +1)


string = input()
combinations(list(string), 0)