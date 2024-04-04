"""
File: MidpointKarel.py
Name: Christina
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *


def turn_around():
    """
    Karel will turn left two times.
    """
    turn_left()
    turn_left()


def move_two_times():
    """
    Karel will move two times.
    """
    move()
    move()


def start():
    """
    pre-condition: Karel is at (1,1), facing East.
    post-condition: Karel is at (1, rightmost-1 of the world), facing West.
    """
    put_beeper()
    while front_is_clear():
        move()
    put_beeper()
    turn_around()
    move()


def back_and_forth():
    """
    pre-condition: Karel is at (1, rightmost-1 of the world), facing West.
    post-condition: Karel is at (1, right next to the midpoint), facing East, with beepers on each of the street 1.
    """
    while not on_beeper():
        move()
    turn_around()
    move()
    put_beeper()
    move()


def remove_redundant_beeper():
    """
    pre-condition: Karel is at (1, right next to the midpoint), facing East, with beepers on each of the street 1.
    post-condition: Karel is at (1,1), facing east. There are only two beepers, one is on the center,
                    another is on right next to the center.
    """
    move()
    while on_beeper():
        pick_beeper()
        if front_is_clear():
            move()
    turn_around()
    while not on_beeper():
        move()
    move_two_times()
    while front_is_clear():
        pick_beeper()
        move()
    pick_beeper()
    turn_around()


def remove_right_next_beeper():
    """
    pre-condition: Karel is at (1,1), facing east. There are only two beepers on the center, right next to the center.
    post-condition: Karel is at (1, midpoint), facing east. There are only one beeper on the center.
    """
    while not on_beeper():
        move()
    move()
    pick_beeper()
    turn_around()
    move()


def checkerboard_type():
    """
    Karel will check on which types of checkerboard he stands.
    """
    if not front_is_clear():  # Avenue = 1
        put_beeper()
    else:
        move()
        if not front_is_clear():  # Avenue = 2
            put_beeper()
        else:
            move()
            if not front_is_clear():  # Avenue = 3
                turn_around()
                move()
                put_beeper()
            else:
                move()
                if not front_is_clear():  # Avenue = 4
                    turn_around()
                    move()
                    put_beeper()
                else:  # the remaining types
                    turn_around()
                    while front_is_clear():
                        move()
                    turn_around()
                    start()
                    while not on_beeper():
                        back_and_forth()
                    remove_redundant_beeper()
                    remove_right_next_beeper()


def main():
    """
    Karel will find the median of the 1st street.
    """
    checkerboard_type()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
