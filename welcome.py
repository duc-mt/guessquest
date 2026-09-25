#!/usr/bin/python3
# -*- coding: utf-8 -*-

# =============================================================================
#
#        FILE:  welcome.py
#      AUTHOR:  Mai Tan Duc <ducmai.network@gmail.com>
#     CREATED:  2021-07-15
# DESCRIPTION:  Introduces the user to the game, asking them to choose level.
#
# =============================================================================

# ------------------------------- Module Imports ------------------------------
"""
The game_options module contains 3 user choices: easy, medium, and hard mode.
It also asks whether the user want to play the game again.
The time.sleep() function gives break between each set of message.
"""
import options as option
from time import sleep


# ---------------------------- Function Definition ----------------------------
def start_game() -> None:
    print('Hello, Welcome to Guessquest!')
    name = input('I\'m Henry! What\'s Your Name? ')
    sleep(1)

    print(f'Okay, {name}. Let\'s Begin Guessquest!')
    print('Choose a level:',
          '1. Easy',
          '2. Medium',
          '3. Hard',
          sep='\n',
          )
    sleep(1)
    try:
        level = int(input('Pick a number: '))
    except ValueError:
        level = 0
    print()
    sleep(1)

    if level == 1:
        option.easy()
        option.try_again()
    elif level == 2:
        option.medium()
        option.try_again()
    elif level == 3:
        option.hard()
        option.try_again()
    else:
        print('ERROR! Invalid value! Please try again.\n')
        start_game()
