# Example of a function that prints a value
# passed to it as a parameter


def print_value(value):
    print(value)


def calculate_gross_pay(hours, rate):
    gross_pay = rate * hours
    print("Your gross pay is {0:.2f}".format(gross_pay))


def main():
    hours_worked = eval(input("hours worked: "))
    pay_rate = eval(input("Your pay rate: "))

    calculate_gross_pay(hours_worked, pay_rate)


if __name__ == '__main__':
    main()
