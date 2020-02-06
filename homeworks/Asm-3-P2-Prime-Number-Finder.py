# Made by Zhongli Liang
import math

# Let the user input a positive number
n = int(input("Enter a positive number: "))

# Check to see if the number is positive, if not, ask the user to enter a new number
while n < 0:
    print("Error: your number is not positive")
    n = int(input("Please Enter a positive number: "))

# creates the flag value, default it to true
flag = True

# use math library to calculate the square root of the number before comparison
n = int(math.sqrt(n))

# An even number is prime if it is 2.
if n == 2:
    flag = True
else:
    for i in range(3, n):  # is prime if it is not divisible by any odd integer - or = to the square root of the num.
        if n % i == 0:
            flag = False  # Set flag to false

# depending on the status of the flag, output the answer.
if not flag:
    print("It's not a prime number")
else:
    print("It's a prime number")
