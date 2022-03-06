#suma w sekundi = vreme 1 + vreme 2 + vreme 3
#vreme v minuti = suma w sekundi / 60
#vremeto v secundi suma w sekundi % 60
#pechatame - {min}:0 {sec}
#ako e >= 10 {min}:{sec}

time1 = int(input())
time2 = int(input())
time3 = int(input())

sum_seconds = time1 + time2 + time3
minutes = sum_seconds // 60
seconds = sum_seconds % 60
if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")


