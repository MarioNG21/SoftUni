# na vseki 50 m se zabavq s 30 sec
# razlika sprqmo rekorda do sega
# zabavqneto se zakruglq kum dolnoto chislo
from math import floor
record_seconds = float(input())
distance_in_meter = float(input())
time_in_seconds_per_1m = float(input())

our_time_in_sec = distance_in_meter * time_in_seconds_per_1m
delay = floor((distance_in_meter / 50)) * 30

our_time_in_sec = our_time_in_sec + delay

if our_time_in_sec < record_seconds:
    print(f"Yes! The new record is {our_time_in_sec:.2f} seconds.")
else:
    needed_time = abs(record_seconds - our_time_in_sec)
    print(f"No! He was {needed_time:.2f} seconds slower.")