# let the user input the current temp
temperature = int(input("Enter the current temperature: "))
# set a constant value that defines the warm threshold for a temp
THRESHOLD = 60

isWarm = temperature > THRESHOLD
# one way decision: one alternative taken if condition holds
if isWarm:
    print("it's warm outside!")
# change it to a two way
else:
    print("it's not warm")

# Create a Boolean variable ( George Bool's name used here)
# it can take only 2 value: True or False
isRaining = True

if isRaining:
    print("It's raining!")
else:
    print("it's not raining")
