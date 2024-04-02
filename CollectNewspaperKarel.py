"""
File: CollectNewspaperKarel.py
Name: Christina
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def turn_around():
    turn_left()
    turn_left()


def pick_newspaper():
    """
    pre-condition: Karel is at (4,3), facing East.
    post-condition: Karel is at (3,6) and picked the newspaper, facing East.
    """
    while front_is_clear():
        move()
    turn_right()
    while not left_is_clear():
        move()
    turn_left()
    while not on_beeper():
        move()
    pick_beeper()


def go_home():
    """
    pre-condition: Karel is at (3,6), facing East.
    post-condition: Karel is at (4,3), facing East, with the newspaper on the table.
    """
    turn_around()
    while front_is_clear():
        move()
    turn_right()
    while front_is_clear():
        move()
    turn_right()
    put_beeper()


def main():
    """
    Karel will pick up the newspaper, go back home, and enjoy the newspaper.
    """
    pick_newspaper()
    go_home()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
