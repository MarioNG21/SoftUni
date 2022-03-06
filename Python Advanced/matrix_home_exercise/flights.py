def flights(*args, dictionary={}):
    if args[0] == "Finish":
        return dictionary
    if str(args[0]).isalpha() and str(args[0]) not in dictionary:
        dictionary[args[0]] = 0
    else:
        pass
    flights(args[1:])


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))

