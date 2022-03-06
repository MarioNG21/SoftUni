
"""
expression = '1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5'
(4, 9, 15
opening = 9
closing = 15 щом е намерена затваряща последната добавена е нейната отваряща 
            -> expression between 9 and 15

след това премахваме отварящата и така накрая остава тази една която и търсим отварящата


closing at 27, opening 21
        -> expressing between 21 and 27


# Notes:
- stack has values after expression is complete,
        -> invalid expression
        значи не е срещнала своята затваряща
- At any moment, is closing is found, and stack is empty
        -> invalid expression


"""

expression = input()
parenthesis_indices = []
for index, ch in enumerate(expression):
    if ch == "(":
        parenthesis_indices.append(index)
    elif ch == ")":
        closing_index = index
        opening_index = parenthesis_indices.pop() # това е последния добавен опънинг и следва че това му е затварящата
        print(expression[opening_index:closing_index+1])
