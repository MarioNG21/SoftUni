period = int(input())
number_of_doctors = 7
treated = 0
untreated = 0
for days in range(1, period+1):
    if days % 3 == 0:
        if untreated > treated:
            number_of_doctors += 1
    patience = int(input())
    if patience <= 7:
        treated += patience
    elif patience > 7:
        untreated += patience - number_of_doctors
        treated += number_of_doctors
print(f"Treated patients: {treated}.")
print(f"Untreated patients: {untreated}.")
