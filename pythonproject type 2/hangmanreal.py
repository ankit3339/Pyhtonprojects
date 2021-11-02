import random
import time

print("What is you name??")
name = input(">>>")
time.sleep(1)

print(f"Welcome to the hangman game {name}")
time.sleep(1)


def game():
    print("You wana play a hangman Game?? y: yes and n: no")
    choice = input(">>>")
    choice.lower()

    if choice == 'y' or choice == 'yes':
        print("The game will be start in few seconds.")
        time.sleep(2)
        print("lets start")
        time.sleep(1)

        words = ["january", "border", "image", "film", "promise", "kids", "lungs", "doll", "rhyme", "damage",
                 "plants"]

        word = random.choice(words)
        print(word)
        guesses = ""
        turns = 5
        hang = 0
        while turns > 0:
            failed = 0
            for char in word:
                if char in guesses:
                    print(char)
                else:
                    print("_")
                    failed += 1
            if failed == 0:
                print("you won")
                break

            guess = input("Enter alphabet")
            guesses += guess
            print(guesses)
            if guesses not in word:
                hang += 1
                turns -= 1
                if hang == 1:
                    print("   _____ \n"
                          "  |     | \n"
                          "  |     |\n"
                          "  |     O\n"
                          "  |      \n"
                          "  |      \n"
                          "  |      \n"
                          "  |      \n"
                          "__|__\n")
                elif hang == 2:
                    print("   _____ \n"
                          "  |      |\n"
                          "  |      |\n"
                          "  |      O\n"
                          "  |      |\n"
                          "  |      |\n"
                          "  |      \n"
                          "  |      \n"
                          "__|__\n")
                elif hang == 3:
                    print("   _____ \n"
                          "  |      |\n"
                          "  |      |\n"
                          "  |      O\n"
                          "  |     /|\ \n"
                          "  |    / | \ \n"
                          "  |      \n"
                          "  |      \n"
                          "__|__\n")
                elif hang == 4:
                    print("   _____ \n"
                          "  |      |\n"
                          "  |      |\n"
                          "  |      O\n"
                          "  |     /|\ \n"
                          "  |    / | \ \n"
                          "  |     /|\ \n"
                          "  |    /   \ \n"
                          "__|__\n")
                elif hang == 5:
                    print("   _____ \n"
                          "  |      |\n"
                          "  |      |\n"
                          "  |      O\n"
                          "  |     /|\ \n"
                          "  |    / | \ \n"
                          "  |     ||| \n"
                          "  |     | | \n"
                          "__|__\n")
                print("turns left", turns)
                if turns == 0:
                    print("you loose")
                    break
    elif choice == 'n' or choice == 'no':
        print("okie, that for your time")
        print("GoodBye")
    else:
        print("try again")
        game()


game()
