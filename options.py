#!/usr/bin/python3
# -*- coding: utf-8 -*-

# =============================================================================
#
#        FILE:  options.py
#      AUTHOR:  Mai Tan Duc <ducmai.network@gmail.com>
#     CREATED:  2021-07-15
# DESCRIPTION:  Determines game modes and the 'try_again' option.
#
# =============================================================================

# ------------------------------- Module Imports ------------------------------
"""
The first module contains the main part of the game, which is processing
the guess and validate user input.
The second module is the introduction to the game, where the user is asked
to choose a mode to play.
"""
from operations import guessing as game
import welcome


# ---------------------------- Function Definitions ---------------------------
def easy() -> None:
    print('You are to guess a number between 1 and 10 '
          'in no more than 6 attempts.')
    game(10, 6)


def medium() -> None:
    print('You are to guess a number between 1 and 20 '
          'in no more than 4 attempts.')
    game(20, 4)


def hard() -> None:
    print('You are to guess a number between 1 and 50 '
          'in no more than 3 attempts.')
    game(50, 3)


def try_again() -> None:
    print()
    again = input('Do you want to play again? [Y/n] ')
    print()
    if again.lower() in ['y', 'yes']:
        welcome.start_game()
    elif again.lower() in ['n', 'no']:
        print('Thanks for playing the game!')
    else:
        print('INVALID VALUE!')
        try_again()
