def squares(n):
    # wrongly squares = [x * x for x in range(n)] goes through every area. Slow !!
    # for x in wrongly squares:
    #   yield x
    # DO NOT DO THIS

    # correct also
    # for x in range(1, n + 1 )
    # yield x * x
    return (x * x for x in range(1, n + 1))


print(list(squares(5)))
