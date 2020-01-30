
# if-else-if structure : multiple condition
"""
Write Python code that convert a percentage grade to letter grade

90-100 = A
80-89 = B
70-79 = C
60-69 = D
below 60 = F
"""

# input grade

grade = eval(input("input your grade here (0-100): "))

# comparison
# use of nesting
"""
if 90 <= grade <= 100:
    print("A")
else:
    if 80 <= grade <= 89:
        print("B")
    else:
        if 70 <= grade <= 79:
            print("C")
        else:
            if 60 <= grade <= 69:
                print("D")
            else:
                print("F")
"""
# Use a multiple way structure: if-elif-else

if grade >= 90:
    print("A")
elif grade >= 80 :
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")
