# Made by Zhongli Liang

# Let the user input a positive number
n = int(input("Enter a positive number: "))

# Check to see if the number is positive, if not, ask the user to enter a new number
while n < 0:
    print("Error: your number is not negative")
    n = eval(input("Please Enter a positive number: "))

flag = True

for i in range(2, n):
    if n % i == 0:
        flag = False

if not flag:
    print("It's not a prime number")
else:
    print("It's a prime number")
