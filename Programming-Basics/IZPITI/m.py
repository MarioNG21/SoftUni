number = float(input())
metric = input()
metric_end = input()

if metric == "mm" and metric_end == "m":
    number = number / 1000
if metric == "mm" and metric_end == "cm":
    number = number / 10
if metric == "cm" and metric_end == "mm":
    number = 10 * number
if metric == "cm" and metric_end == "m":
    number = number / 100
if metric == "m" and metric_end == "cm":
    number = 100 * number
if metric == "m" and metric_end == "mm":
    number = 1000 * number
print(f"{number:.3f}")