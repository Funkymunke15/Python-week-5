# Davis Arita
# 9/26/22
# CS 131 Exercise 5 part A
# prints a given string with very second letter of the string removed or
# with all the vowels replaced by an underscore

# takes user input
input = input("Enter a string: ")

counter = 0
strlen = len(input)
newString = ""


for index in range(0, strlen, 2):
    newString += input[index]


print("The string with every second letter printed is:", newString)
newString = ""
counter = 0
VOWELS = "aeiou"
while counter < strlen:
    if input[counter].lower() in VOWELS:
        newString += "_"
    else:
        newString += input[counter]
    counter += 1
print("The string with every vowel replaced with  _ is:", newString)

