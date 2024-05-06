# Davis Arita
# 9/28/22
# CS 131 Lecture 5A lab 2
# counts the number of vowels in a string using while loop

input = input("Enter a string: ")
VOWELS = "aeiou"
i = 0
counter = 0
while counter < len(input):
    if input[counter].lower() in VOWELS:
        i += 1
    counter += 1
print("The string has %d vowels." % i)
