# generate a random number between 1 and 10
import random


def game():
    """lets player play the game.
    generates a random number.
    asks player to guess the number.
    If the player's guess is too high, tell him so.
    If the player's guess is too low, tell him so.
    prints win/lose messages at the end of each run.
    gives player options to play again.
    """
    secret_num = random.randint(1, 10)
    guesses = []

    while len(guesses) < 5:
        try:
            # get a number guess from the player
            guess = int(input("Guess a number between 1 and 10: "))
        # catch when someone submits a non-integer
        except ValueError:
            print("{} isn't a number!".format(guess))
        else:
            # compare guess to secret number
            # print hit/miss
            if guess == secret_num:
                print("You got it! My number was {}".format(secret_num))
                break
            # print "too low" or "too high" messages for bad guesses
            elif guess < secret_num:
                print("My number is higher than {}".format(guess))
            else:
                print("My number is lower than {}".format(guess))
            # limit the number of guesses
            guesses.append(guess)
    else:
        print("You didn't get it! My number was {}".format(secret_num))
    # let people play again
    play_again = input("Do you want to play again? Y/n ")
    if play_again.lower() != "n":
        game()
    else:
        print("Bye!")


game()
