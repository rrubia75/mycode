#!/usr/bin/env python3
import csv
from time import sleep
pokenum= input(">")
with open("pokedex.txt","r") as pokedata:
    for x in csv.DictReader(pokedata):
        pokedict= dict(x)
        if pokedict["#"] == pokenum:
            print(f"{pokedict['Name']} is of the {pokedict['Type 1']} and {pokedict['Type 2']} types!")
            sleep(1)
            x= input("Would you like to know the Attack and Special Attack base stats? ")
            if x == "yes":
                print(f"{pokedict['Name']} has an attack stat of {pokedict['Attack']} and a Special Attack stat of {pokedict['Sp. Atk']}")
            elif x == "no":
                print("Ok, Thank you for playing")
            else:
                print("You were supposed to type yes or no dummy. Now you need to run this script again")
