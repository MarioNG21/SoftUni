series = input()
number_of_seasons = int(input())
number_of_episodes = int(input())
duration_without_ads = float(input())

ads = 0.2 * duration_without_ads
duration_with_ads = duration_without_ads + ads
one_season = duration_with_ads * number_of_episodes
spec_episode = 10 * number_of_seasons
whole_time = one_season * number_of_seasons + spec_episode
print(f"Total time needed to watch the {series} series is {round(whole_time)} minutes.")