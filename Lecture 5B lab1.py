# Davis Arita
# 9/28/22
# CS131 Lecture 5B lab 1
# prints a table of triangle numbers up to the user imputed number

num1 = int(input("Enter a positive integer n: "))

for i in range(1, num1+1):
    print("n = {0}, triangle = {1}".format(i, (i ** 2 + i) // 2))

