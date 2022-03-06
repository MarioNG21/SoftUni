# suma = depozit suma + srok na depozit * (depozit suma * godishana
deposit_sum = float(input())
months = int(input())
percent = float(input())


sum = deposit_sum + months * ((deposit_sum* (percent / 100)) /12 )
print(sum)
