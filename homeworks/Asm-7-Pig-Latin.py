# Made by Shiina Yuri

string = input("Input Sentence in ALL CAPS:")  # Let user input the sentence, save it as a string

string = string.split()  # Split the string into a list

print("The Sentence in Pig Latin:")  # Tell the user that the line below will be pig latin
for word in string:   # Loop through the list and change every word to Pig Latin
    print(word[1:] + word[0] + "AY", end=" ")  # Print out the words as well

print()
