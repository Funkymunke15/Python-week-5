# Davis Arita
# 9/28/22
# CS 131 Lecture 5B lab 2
# prints a multiplication table for the first n numbers
dash = "-----"
n = int(input("Enter n: "))
print("  | ", end="")
for col in range(1, n+1):
    print("%-4.d" % col, end=" ")
print("\n", dash*n)
for row in range(1, n+1):
    print("%2.d" % row, end="| ")
    for col in range(1, n+1):
        print("%-4.d" % (row*col), end=" ")
    print()

