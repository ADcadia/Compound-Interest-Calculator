# Enter the number of times you will toss the coin. 

import random

def tossCoin():
  num = random.randint(0, 1)
  if num == 0:
    return "Heads"
  else:
    return "Tails"

timesToToss = int(input("How many times will you toss the coin? \n"))
headsCounter = 0
tailsCounter = 0

for i in range(timesToToss):
  if tossCoin() == "Heads":
    headsCounter = headsCounter+1
  else: 
    tailsCounter = tailsCounter+1

print("Heads: ", headsCounter, "\nTails: ", tailsCounter)
