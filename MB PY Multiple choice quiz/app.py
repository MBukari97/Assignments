print("Welcome to my quiz")

playing = input ("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay, Let the quiz begin!")

answer = input("How many billionaires are there living in the uk? \n(a) 112\n(b) 171\n(c) 149\n\n",)
if answer == "b":
    print("You are correct!")
else:
    print('You are wrong')

answer = input("What year did apple launch their first iPhone? \n(a) 2007\n(b) 2006\n(c) 2009\n\n",)
if answer == "a":
    print("You are correct!")
else:
    print("You are wrong")


answer = input("Where did Arsenal use to play their home games before playing in their current home ground Emirates Stadium? \n(a) White Heart Lane\n(b) Highbury\n(c) Craven Cottage\n\n",)
if answer == "b":
    print("You are correct!")
else:
    print("You are wrong")
