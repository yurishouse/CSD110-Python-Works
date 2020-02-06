# Simple function that prints a message
def print_message():
    x = 100  # local to this function not the others
    print("Hello World", x)


# function call : function is a dormant code that needs to be called to run
# print_message()


# we are turning a script into a program
def main():
    # print(x)
    # illegal to reference a local variable of another function because its not visible
    print_message()


if __name__ == '__main__':
    main()
