import random

guess = random.randrange(1, 50)
number = int(input("Guess the number between 1 to 50 \n"))

while guess != number:
    if guess > number:
        number = int(input(" guess greater \n"))
    else:
        number = int(input(" guess less \n"))

print("the answer is correct ", number)
