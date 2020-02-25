
# Example of empty dictionary

courses = {}

# Another way

data = dict()


# Adding to a dictionary: Using the key as an index
# use course code as a key and the title as value

courses["CSD110"] = "Python"
courses["CS&141"] = "Java I"

print(courses)

# Building a dictionary with initial values

stateCapitals = {
    'WA': 'Olympia',
    'OR': 'Salem',
    'CA': 'Sacramento'
}
print(stateCapitals)

# Using index
print("The capital of WA is", stateCapitals['WA'])

# Looping
for state in stateCapitals:
    print(state, end=' ')
print()

# Print all the capital cities
for state in stateCapitals:
    print(stateCapitals[state], end=' ')
print()

# access both key and value
# Using items method

for key, value in stateCapitals.items():
    print(key, value, sep=':')
print()

# Lookup the numbers of records in a dictionary

print(len(stateCapitals))

# Define an empty dictionary useful for storing the world's
# Capital cities
# Add countries to it
# Print it out using print or looping

worldCapital = {
    'China': 'Beijing',
    'US': 'New York',
    'England': "London",
    'Japan': 'Tokyo',
    'France': 'Paris'
}
for c, ci in worldCapital.items():
    print(c, ci, sep=' : ')

# Remove a item from a dictionary
del worldCapital['China']

print(worldCapital)

# clear everything from a dictionary
# worldCapital.clear()
# print(worldCapital)

# To access an item in the dictionary

# Better way (No key error)

print("I'm currently in", worldCapital.get('US'))

# list the values in dictionary

print(worldCapital.values())

# randomly pop an item

print(worldCapital.popitem())
print(worldCapital)

"""
Write python code to request course title from a user given a list of courses that you're  
taking or a part of your program plan and populate a dictionary with the data

"""

courses = ['CSD110', 'CSD112', "PSYC100", "SOCL100", "CMST100"]
description = {}
for classes in courses:
    info = input("input the class info for {0:} here: ".format(classes))
    description[classes] = info
print(description)
