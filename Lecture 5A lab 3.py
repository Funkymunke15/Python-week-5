# Davis Arita
# 9/26/2022
# CS 131 Lecture 5A lab 4
# computes the number of passing and failing grades,computes the average grade
# and finds the highest and lowest grade.
SENTINEL = -1
grade = 0
count = 0
passing = 0
failing = 0
total = 0
highest = 0
lowest = 100
average = 0
done = False
while not done:
    grade = int(input("Enter a grade or -1 to finish: "))
    if grade < 0:
        done = True
    else:
        total += grade
        count += 1
        if grade >= 60:
            passing += 1
            if grade > highest:
                highest = grade
        else:
            failing += 1
            if grade < lowest:
                lowest = grade
if count == 0:
    average = 0
else:
    average = total/count
    print("The average grade is %.2f " % average)
    print("Number of passing grades is %d " % passing)
    print("Number of failing grades is %d " % failing)
    print("The maximum grade is %.2f " % highest)
    print("The minimum grade is %.2f " % lowest)
