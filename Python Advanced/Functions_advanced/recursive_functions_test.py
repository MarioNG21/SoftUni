def f1(index, max_index):
    print(f' --loop({index}, {max_index})-- ')

    if index == max_index:
        print(f' --ending loop({index},{max_index} )-- ')
        return
    print(index)
    f1(index=index + 1, max_index=max_index)
    print(f' --ending loop({index}, {max_index} )-- ')


f1(0, 10)