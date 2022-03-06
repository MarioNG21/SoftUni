# да избере филм с най-висок рейтинг (максзайз)
# да избере филм с най- нисък рейтинг
# средният рейтинг
from sys import maxsize
max_rating = - maxsize
min_rating = maxsize
number_of_films = int(input())

sum_of_ratings = 0
max_rating_movie = ""
min_rating_movie = ""
for film in range(1, number_of_films+1):
    name_of_movie = input()
    rating = float(input())
    if rating < min_rating:
        min_rating = rating
        min_rating_movie = name_of_movie
    if rating > max_rating:
        max_rating = rating
        max_rating_movie = name_of_movie
    sum_of_ratings += rating
print(f"{max_rating_movie} is with highest rating: {max_rating:.1f}")
print(f"{min_rating_movie} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {sum_of_ratings/number_of_films:.1f}")