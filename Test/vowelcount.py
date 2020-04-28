# Made by Zhongli Liang
def numbers_total(num):  # Defines numbers_total method
    total = 0  # local variable
    for i in range(len(num)):  # Loop through each character
        number = int(num[i])  # Convert the character to an integer.
        total += number  # Add the value to the running total.
    return total  # Return the result


def main():
    numbers = input('Enter the numbers with no separation: ') # Get a string of numbers as input from the user.
    total = numbers_total(numbers)  # Call numbers_total method and given the input, store the returned total.
    print('The total of the numbers is {0:}'.format(total))  # Display the total.


if __name__ == '__main__':  # Call for main function
    main()