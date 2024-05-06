# Davis Arita
# 9/26/2022
# CS 131 Exercise 6 Part C
# basic ticket selling program

TOTAL_TICKETS = 40
ticketsSold = 0
currentTickets = TOTAL_TICKETS
numBuyers = 0
print("There are currently %d tickets remaining." % currentTickets)
while currentTickets > 0:
    userInput = int(input("How many tickets would you like to purchase? "))
    if userInput > 10 or userInput <= 0:
        print("Sorry, you can't buy that many.")
    else:
        currentTickets -= userInput
        numBuyers += 1
        if currentTickets == 0:
            print("The total number of buyers was %d" % numBuyers)
        else:
            print("There are currently %d tickets remaining." % currentTickets)

