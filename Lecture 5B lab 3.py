# Davis Arita
# 9.28.22
# CS 131 Lecture 5B lab 3
# prints the number of lower case letters, upper case letters, digits, and
# special symbols in a string

str = input("Please enter a string: ")
lowerNum = 0
upperNum = 0
digitNum = 0
symbolNum = 0
for index in str:
    if index.islower():
        lowerNum += 1
    elif index.isupper():
        upperNum += 1
    elif index.isdigit():
        digitNum += 1
    elif not index.isalnum():
        symbolNum += 1

print("Total count of lowercase char: %d" % lowerNum)
print("Total count of uppercase char: %d" % upperNum)
print("Total count of digits: %d" % digitNum)
print("Total count of symbols: %d" % symbolNum)