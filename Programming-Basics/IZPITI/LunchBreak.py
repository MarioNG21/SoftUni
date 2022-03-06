from math import ceil
series = input()
duration_of_one_episode = int(input())
duration_of_break = int(input())

lunch_time = 1/8 * duration_of_break
lazy_time = 1/4 * duration_of_break

left_time_for_episode = duration_of_break - (lazy_time + lunch_time)
if duration_of_one_episode > left_time_for_episode:
    diff = ceil(duration_of_one_episode - left_time_for_episode)
    print(f"You don't have enough time to watch {series}, you need {diff} more minutes.")
else:
    left_time = ceil(left_time_for_episode - duration_of_one_episode)
    print(f"You have enough time to watch {series} and left with {left_time} minutes free time.")