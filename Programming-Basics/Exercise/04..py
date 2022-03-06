number_pages = int(input())
pages_per_hour = int(input())
number_days = int(input())
needed_pages_per_day = number_pages / pages_per_hour
needed_time =  needed_pages_per_day / number_days
print(needed_time)
