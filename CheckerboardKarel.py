"""
File: CheckerboardKarel.py
Name: Christina
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *


def turn_around():
    """
    Karel will turn left 2 times.
    """
    turn_left()
    turn_left()


def turn_right():
    """
    Karel will turn left 3 times.
    """
    turn_left()
    turn_left()
    turn_left()


def put_chess_odd():
    """
    Karel is on the odd number of avenue.
    pre-condition: Karel is at (1, odd avenue), facing East
    post-condition: Karel is at (top of the checkerboard, odd avenue), facing North
    """
    turn_left()
    put_beeper()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()


def put_chess_even():
    """
    Karel is on the even number of avenue.
    pre-condition: Karel is at (1, even avenue), facing East
    post-condition: Karel is at (top of the checkerboard, even avenue), facing North
    """
    turn_left()
    move()
    put_beeper()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()


def go_back():
    """
    Karel will return to the floor of the checkerboard.
    pre-condition: Karel is facing North somewhere
    post-condition: Karel is at (1, ?), facing East
    """
    turn_around()
    while front_is_clear():
        move()
    turn_left()


def check_front():
    """
    Karel will check if there is any chess on the front.
    """
    if not on_beeper():
        turn_left()
        move()
        if not on_beeper():
            go_back()
            check_left()
        else:
            go_back()


def check_left():
    """
    Karel will check the previous checkerboard's type.
    """
    turn_around()
    move()
    if on_beeper():
        turn_around()
        move()
        put_chess_odd()
    else:
        turn_around()
        move()
        put_chess_even()


def check_position():
    """
    Karel will check whether he has finished the checkerboard.
    pre-condition: Karel is at (end floor of the checkerboard, ?), facing East
    post-condition: Karel is at (1, ?), facing East
    """
    check_front()


def checkerboard_type():
    """
    Karel will check on which types of checkerboard he stands.
    """
    if not front_is_clear():
        if not left_is_clear():  # 1*1
            put_beeper()
        else:  # 1*?
            put_chess_odd()
    else:
        if not left_is_clear():  # ?*1
            turn_right()
            put_chess_odd()
        else:  # the remaining types
            while front_is_clear():
                put_chess_odd()
                go_back()
                if front_is_clear():
                    move()
                    put_chess_even()
                    go_back()
                    if front_is_clear():
                        move()
            check_position()


def main():
    """
    Karel will build a checkerboard.
    """
    checkerboard_type()



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
