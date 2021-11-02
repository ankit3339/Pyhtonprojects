import random

name = input("What is your name : ")
print("Welcome {}, Lets play a hangman game".format(name))

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)
print(word)

guesses = ''

turns = 12

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print('_')
            failed += 1

    if failed == 0:
        print("you won, {} ".format(name))
        print("the word is {}".format(word))
        break

    guess = input("Guess the character")

    guesses += guess

    if guess not in word:
        turns -= 1
        print("wrong!!\n")
        print("turns left {}\n".format(turns))
        if turns == 0:
            print("you loose {}".format(name))
