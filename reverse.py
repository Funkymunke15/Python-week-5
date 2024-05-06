# Davis Arita
# 9/26/2022
# CS 131 Exercise 6 part B
# prints a string in reverse

string = input("Enter a word: ")
strLen = len(string)

count = strLen-1
newString = ""
while count >= 0:
    newString += string[count]
    count -= 1

print(string, "reversed is", newString)


