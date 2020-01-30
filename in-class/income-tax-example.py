"""
Write python code to calculate the income tax for user
base on the following rate
80,000 or +  / 20%
50,000 to/and 80.000 / 15%
25.000 to/and 50.000 / 10%
below 25.000 / 0%

the user enters the income and you should output the tax owed
taxOwed = income * taxRate/100
"""
# income input
income = eval(input("Input your income here: "))

# compare with rate
if income >= 80000:
    taxRate = int(20)
elif 50000 <= income:
    taxRate = int(15)
elif 25000 <= income:
    taxRate = int(10)
else:
    taxRate = 0
# Calculations of taxOwed using taxRate
taxOwed = income * taxRate/100

# Print the result
print("You owe ${:.2f} of tax" .format(taxOwed))
