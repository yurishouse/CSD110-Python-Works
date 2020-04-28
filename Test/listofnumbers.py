# Made by Zhongli Liang


def main():  # define main function
    # create an empty list
    numbers = []
    # loop 20 time to let the user input the number
    for i in range(20):
        numbers.append(eval(input('{0:} input a number: '.format(i))))  # append the input number to list 'numbers'
    # Print the lowest number using min function
    print('The lowest number is', min(numbers))
    # Print the highest number using max function
    print('The highest number is', max(numbers))
    # Print the total using sum function
    print('The total of the numbers are', sum(numbers))
    # Print the average using sum of the numbers / by 20
    print('The average of the numbers are {0:.3f}'.format(sum(numbers) / 20))


if __name__ == '__main__':  # Call for main function
    main()
