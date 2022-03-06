from math import pi
shape = "square"
shape_2 = "rectangle"
shape_3 = "circle"
shape_4 = "triangle"

if shape:
    side = float(input())
    print(f"{side * side:.3f}")
if shape_2:
    side_1 = float(input())
    side_2 = float(input())
    area = side_1 * side_2
    print(f"{area:.3f}")
if shape_3:
    radius = float(input())
    area = pi *(radius*radius)
    print(f"{area:.3f}")
if shape_4:
    height = float(input())
    weight = float(input())
    area = (height * weight) / 2
    print(f"{area:.3f}")