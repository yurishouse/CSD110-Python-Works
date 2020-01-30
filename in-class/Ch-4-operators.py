
# Augmented operators

x = 100

x += 20

print("Adding 20 to x", x)

x -= 20

print("Subtracting 20 from x", x)

x *= 10

print("multiply x by 10", x)

x /= 5

print("Dividing x by 5", x)

x %= 11

print("compressing x by 11", x)

# example of a running total accumulator
# adding the first (n) 100 numbers 1..100 = 5050 (n *(n + 1)/2)

sums = 0

for number in range(1, 101):
    sums += number

print("Sum of the first 100 numbers are expected (5050)", sums)

# Calculating factorial of a number: 20
"""
f = 1

for i in range(1, 21):
    f *= number

print('Factorial of number 20', f)
"""

n = eval(input("Enter a positive number: "))

# Validate the number is negative

while n < 0:
    print("Error: your number is not negative")
    n = eval(input("Enter a positive number: "))

# Exit(1)

f = 1

for i in range(1, n+1):
    f *= i

print(n, "! = ", f, sep='')

