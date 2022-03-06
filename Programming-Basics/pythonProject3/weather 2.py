grade = float(input())
if 26.00 <= grade <= 35.00:
 print ("Hot")
elif 20.1 <= grade and grade <= 25.9:
     print ("Warm")
elif 15.00 <= grade and grade <= 20.00:
     print ("Mild")
elif 12.00 <= grade and grade <= 14.9:
     print ("Cool")
elif 5.00 <= grade and grade <= 11.9:
     print ("Cold")
else:
    print("unknown")

