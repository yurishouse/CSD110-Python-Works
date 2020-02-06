import math


# Position arguments

# Change the function so that it does not print the volume
#  but return the result to the sender
def cylinder_volume(height, radius):
    volume = height * math.pi * radius ** 2
    return volume


def main():  # Scope of the main program logic
    h = 300
    r = 20
    vol = cylinder_volume(h, r)
    # Using position arguments
    # cylinder_volume(radius=r, height=h)
    print("volume is {0:.3f}".format(vol))


if __name__ == '__main__':
    main()
