# Made by Shiina Yuri

sp = eval(input("What is the speed of the vehicle in mph? : "))  # Ask the user to input the speed of the vehicle
hours = eval(input("How many hours has it traveled? : "))  # Ask the user to input the hours traveled

hours = hours + 1  # To fix the issue where range does not loop the last number

print("Hour    Distance Traveled")  # To tell the user which number represent which value

for t in range(1, hours, 1):  # Create a loop that go through each hour and calculates the distance
    print(t, end='    ')  # Print out the hour, given some spacing to the distance
    dist = t * sp  # Calculate the distance at current hour
    print(dist, end='')   # Printout distance
    print()  # Go to next line

