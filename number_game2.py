# Try to build the opposite of this game.
# Make a game where the computer tries to guess your secret number.
# You'll need to come up with a way to tell the computer if it's too high, too low, or if it guesses the number!

import random

def game():
    valid_user_guess = False
    while not valid_user_guess:
        try:
            # get a number from the user
            user_num = int(input("Give me a number between 1 and 100: "))
        except ValueError:
            print("Not a valid number.")
        else:
            if user_num < 1 or user_num > 100:
                print("Please guess number between 1 and 100")
            else:
                valid_user_guess = True
                print("Enjoy the game!!!\n")

    guesses = [ ]
    min = 1
    max = 100

    while len(guesses) < 5:
        computer_guess = random.randint(min,max)

        guesses.append(computer_guess)

        # compare computer's guess with user's number
        if computer_guess == user_num:
            print("You won this time. You took {} guesses".format(len(guesses)))
            break
        elif computer_guess < user_num:
            print("My number is higher than {}".format(computer_guess))
            min = computer_guess + 1
        else:
            print("My number is lower than {}".format(computer_guess))
            max = computer_guess - 1
    else:
        print("You didn't get it. My number was {}".format(user_num))

    play_again = input("Do you want to play again? Y/n ")
    if play_again.lower() != "n":
        game()
    else:
        print("Bye!")

game()
