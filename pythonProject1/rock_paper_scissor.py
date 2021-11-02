import random
import math

print("Welcome to the rock paper and scissor game\n")


def game():
    user = input("Enter (r) for Rock, (p) for paper, (s) for scissor\n")
    user = user.lower()

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 0, user, computer
    if is_win(user, computer):
        return 1, user, computer

    return -1, user, computer


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (
            player == 's' and opponent == 'p'):
        return True
    return False


def play_best(n):
    player_win = 0
    computer_win = 0
    wins_necessary = math.ceil(n / 2)
    while player_win < wins_necessary and computer_win < wins_necessary:
        result, user, computer = game()
        if result == 0:
            print("your choice and computer choice is {}, its a tie".format(user, computer))
        elif result == 1:
            player_win += 1
            print("your choice {} , and opponent choice {}, its a win".format(user, computer))
        else:
            computer_win += 1
            print("Your choice {} , and computer choice {}, its a lose".format(user, computer))

    if player_win > computer_win:
        print("congrast you have won the best of {} game".format(n))
    else:
        print("You loose the game")


play_best(3)
