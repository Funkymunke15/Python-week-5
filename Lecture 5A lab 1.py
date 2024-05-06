# Davis Arita
# 9/26/2022
# CS 131 In class lecture 5A lab 1
# using a while loop, print all positive numbers divisible by 5 or 10 and less than n


num1 = int(input("Enter a number: "))

count = 1
while count < num1:
    if count % 5 == 0:
        print(count)
    count += 1

