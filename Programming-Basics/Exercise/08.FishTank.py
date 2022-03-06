# obem(kubichni cm ) = diljina(Cm) * shirochina(cm) * wisochina(cm)
# obem kubichini cm /1000 = obem v litri
# procent zaeta chast ot akvariuma ->/100-> chislo
#litri * (100%- procent zaeta chast)= litri* (1- chislo zaeta chast)
#print
length = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume = length * width * height
volume_liters = volume / 1000
occupied_part = percent / 100
need_liters = volume_liters * (1 - occupied_part)
print(need_liters)

