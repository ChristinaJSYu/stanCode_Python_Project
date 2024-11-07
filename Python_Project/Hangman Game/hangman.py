"""
File: hangman.py
Name: Christina
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def check_legal_case(case):
    """
    You will ensure the case is legal and is uppercase.
    """
    while not case.isalpha() or not len(case) == 1:
        print("Illegal format.")
        case = input("Your guess: ")
    if case.islower():
        return case.upper()
    else:
        return case


def main():
    """
    You will create the hangman game.
    """
    ans = random_word()
    guess_result = ""   # record '-' and correct words
    for i in range(len(ans)):
        guess_result += '-'
    print("The word looks like: " + guess_result)
    print("You have " + str(N_TURNS) + " wrong guesses left.")
    count_life = N_TURNS   # count how many chances of guess you left
    while True:
        if count_life == 0:   # used up all chances of guess, challenge failed
            print("You are completely hung:(")
            print("The answer is: " + ans)
            break
        elif guess_result == ans:   # challenge succeeded!
            print("You win!!!")
            print("The answer is: " + ans)
            break
        else:
            guess = input("Your guess: ")
            guess = check_legal_case(guess)
            temp = ""  # a temp string to record new guess result
            temp_count_life = count_life  # a temp count to record how many chances of guess you left
            for i in range(len(ans)):
                if guess == ans[i]:   # guess correct
                    for j in range(len(ans)):   # use temp string to concatenate new guess result
                        if i == j:
                            temp += guess
                        elif guess_result[j] != '-':
                            temp += guess_result[j]
                        else:
                            temp += '-'
                    guess_result = temp
                    temp = ""
                    temp_count_life += 1
            if temp_count_life != count_life:
                print("You are correct!")
                if guess_result != ans:   # this turn is not the final turn
                    print("The word look like: " + guess_result)
                    print("You have " + str(count_life) + " wrong guesses left.")
            else:
                count_life -= 1
                print("There is no " + guess + "'s in the word.")
                if count_life != 0:   # this turn is not the final turn
                    print("The word look like: " + guess_result)
                    print("You have " + str(count_life) + " wrong guesses left.")


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
