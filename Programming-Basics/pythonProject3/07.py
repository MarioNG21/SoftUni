#1 литър зленеа боя за 3.4 кубични метра
#1 литър червена боя за 4.3 кубични метра
#предната страна е квадрат но трябва от нея да извадим врата с размер 1.2 широчина и 2 височина, а задната си е също квадрат
#страничните страни са правоъглници, на двете страни има квадратни прозорци с размер 1.5
#покривът има 2 правоъгълника с размери х и у пък тръгълниците са с размер х и h

height_of_house = float(input())
wide_of_house =  float(input())
height_of_roof = float(input())

front_plus_back_wall = 2 * (height_of_house * height_of_house) - 2.4
side_wall_sum = 2 * (height_of_house * wide_of_house ) - 4.5

sum_of_walls = front_plus_back_wall + side_wall_sum

green_paint = sum_of_walls / 3.4

both_triangle_roof = (height_of_house * height_of_roof)
both_rectangle_roof =  2 * (height_of_house * wide_of_house)
sum_of_roof = both_rectangle_roof + both_triangle_roof

red_paint = sum_of_roof / 4.3

print(f"{green_paint:.02f}")
print(f"{red_paint:.02f}")


