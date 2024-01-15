# Write a python program to print the frequency of each of the characters present in a given string

string_input = input("Enter you string here : ")
character_occurences = {}
for character in string_input :
    if character.isalpha() :
        char = character.lower()
        character_occurences[char] = character_occurences.get(char , 0) + 1
print(character_occurences)