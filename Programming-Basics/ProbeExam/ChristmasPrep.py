number_rolls_with_paper = int(input())
number_rolls_with_cloth = int(input())
glue = float(input())
discount = int(input())

sum_paper = number_rolls_with_paper * 5.80
sum_cloth = number_rolls_with_cloth * 7.20
sum_glue = 1.20 * glue
discount_in_percent = discount / 100

whole_sum = sum_paper + sum_cloth + sum_glue
whole_sum_with_discount = whole_sum - discount_in_percent * whole_sum
print(f"{whole_sum_with_discount:.3f}")