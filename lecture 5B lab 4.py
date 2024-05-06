# Davis Arita
# 9.28.22
# CS 131 Lecture 5B lab 4
# The simplest math problem no one can solve

import random

n = random.randint(1, 20)
steps = 0
print("The value of n is %d" % n)
while n != 1:
    if n % 2 == 0:
        n /= 2

    else:
        n = (n * 3) + 1
    print(n)
    steps += 1
print("The total stopping time is %d" % steps)

