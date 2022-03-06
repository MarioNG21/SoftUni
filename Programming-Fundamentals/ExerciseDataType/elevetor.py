from math import  ceil
people = int(input())
capacity = int(input())

number_of_courses = ceil(people/capacity)
print(number_of_courses)
