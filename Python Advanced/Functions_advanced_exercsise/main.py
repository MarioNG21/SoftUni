def fill_the_box(h, l, w, *args):
    area = h * l * w
    left_cubes = 0
    list_of_args = list(args)
    has_failed = False
    while list_of_args:
        el = list_of_args[0]
        if el == "Finish":
            break
        area -= el
        list_of_args.pop(0)
        if area <= 0:
            has_failed = True
            list_of_args.pop()
            left_cubes += sum(list_of_args)
            left_cubes -= area
            break
    if has_failed:
        return f"No more free space! You have {left_cubes} more cubes."
    else:
        return f"There is free space in the box. You could put {area} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))