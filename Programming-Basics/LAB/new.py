from math import pi
shape = (input())

if shape == "square":
    side = float(input())
    print(f"{side * side:.3f}")
if shape == "rectangle":
    side_1 = float(input())
    side_2 = float(input())
    area = side_1 * side_2
    print(f"{area:.3f}")
if shape == "circle":
    radius = float(input())
    area = pi *(radius*radius)
    print(f"{area:.3f}")
if shape == "triangle":
    height = float(input())
    weight = float(input())
    area = (height * weight) / 2
    print(f"{area:.3f}")