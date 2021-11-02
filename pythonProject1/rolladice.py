import random
import sys


def roll():
    dice = random.randrange(1, 6)
    print(dice)
    choice = input("do you want to roll a dice again?Y/N")
    if choice == "Y" or choice == "y":
        roll()
    else:
        sys.exit()




roll()
