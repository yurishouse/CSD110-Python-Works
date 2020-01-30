MIN_GPA = 2.0

gpa = eval(input("Enter Your GPA: "))

hasFinancial = eval(input("Do you have financial Aid True/False: "))
"""
if gpa >= MIN_GPA:
    if hasFinancial:
        print("Congrats! You are admitted!")
    else:
        print("Sorry, You need a Financial Aid")
else:
    print("Sorry, you're denied due to low GPA")
"""
# Optimized version using And
"""
if gpa >= MIN_GPA and hasFinancial:
        print("Congrats! You are admitted!")
else:
    print("Sorry, you're denied.")

"""
# Optimized version using or
"""
if gpa < MIN_GPA or hasFinancial == False:
    print("Sorry, you're denied.")
else:
    print("Congrats! You are admitted!")
"""
# Optimized version using not
if gpa >= MIN_GPA or not hasFinancial:
    print("Congrats! You are admitted!")
else:
    print("Sorry, you're denied.")
