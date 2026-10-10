"""
==============================================================================
Module Name:   options.py
Description:   Source module options.py.
Author:        Mai Tan Duc <ducmai.network@gmail.com>
Created:       2026-10-10
Version:       1.0.0
License:       MIT
==============================================================================
Usage:         python3 options.py [options]
Notes:         Requires Python 3.8+
==============================================================================
"""

#!/usr/bin/python3
import welcome
from operations import guessing as game


# ---------------------------- Function Definitions ---------------------------
def easy() -> None:
    print("You are to guess a number between 1 and 10 in no more than 6 attempts.")
    game(10, 6)


def medium() -> None:
    print("You are to guess a number between 1 and 20 in no more than 4 attempts.")
    game(20, 4)


def hard() -> None:
    print("You are to guess a number between 1 and 50 in no more than 3 attempts.")
    game(50, 3)


def try_again() -> None:
    print()
    again = input("Do you want to play again? [Y/n] ")
    print()
    if again.lower() in ["y", "yes"]:
        welcome.start_game()
    elif again.lower() in ["n", "no"]:
        print("Thanks for playing the game!")
    else:
        print("INVALID VALUE!")
        try_again()
