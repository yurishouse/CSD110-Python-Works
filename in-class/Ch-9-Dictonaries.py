
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
    'Japan': 'Tokyo'
    
}
for c, ci in worldCapital.items():
    print(c, ci, sep=' : ')





