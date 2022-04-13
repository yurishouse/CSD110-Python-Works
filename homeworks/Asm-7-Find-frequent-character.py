# Made by Shiina Yuri


sentence = input('Enter some words here: ')  # Let user input a string

sentence = sentence.lower()  # convert everything to lower case

count = 0  # Setup a count variable to be use in the loop
total_count = 0  # Setup a total counter

most_freq_character = ""   # Setup a variable that will store the final result

for ch in sentence:  # Used to zero out the count variable during each loop cycle,
    # also decide which character is looping
    for string in sentence:  # A second loop
        if string == ch:  # if the character that's currently looping is found, it adds 1 to the count variable
            count += 1
    if count > total_count:  # compare the most frequent characters in terms oif times
        total_count = count
        most_freq_character = ch  # Set the Most frequent character
    count = 0  # Zero out counter during each cycle

print("The most frequent character is", most_freq_character, "and it appears", total_count, "times.")
# Print the result
