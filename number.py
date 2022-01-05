#!/usr/bin/env python3

import random

z=random.randint(0,1000)
y=random.randint(0,1000)
while input("Would you like a random number? (yes/no) ") != "yes".lower():
    print("C'mon, you know you want one")
print("Here is your random number: " +str(z))

while input("Would you like another? (yes/no) ") != "yes":
        print("That cannot be correct!")
print("Here is another: " +str(y))

a=input("Would you like another random number? (yes/no) ")
if a == "yes".lower():
    print("I think you've had enough")
elif a == "no".lower():
    print("That's probably for the best")
else:
    print("You have to choose yes or no, dummy")


