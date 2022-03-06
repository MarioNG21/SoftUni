first_figure_first_number = int(input())
second_figure_first_number = int(input())
first_figure_second_number = int(input())
second_figure_second_number = int(input())
count = 0

for first_figure_first in range(first_figure_first_number, 9):
    for second_figure_first in range(9, second_figure_first_number-1, ):
        for first_figure_second in range(first_figure_second_number, 9):
            for second_figure_second in range(9, second_figure_second_number - 1, ):
                if first_figure_first % 2 == 0 and second_figure_first % 2 == 1:
                    if first_figure_second % 2 == 0 and second_figure_second % 2 == 1:
                        if first_figure_first == first_figure_second and second_figure_first == second_figure_second:
                            print("Cannot change the same player.")
                        else:
                            print(f"{first_figure_first}{second_figure_first} - {first_figure_second}{second_figure_second}")
                            count += 1
                            if count == 6:
                                exit()
