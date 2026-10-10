"""
==============================================================================
Module Name:   welcome.py
Description:   Source module welcome.py.
Author:        Mai Tan Duc <ducmai.network@gmail.com>
Created:       2026-10-10
Version:       1.0.0
License:       MIT
==============================================================================
Usage:         python3 welcome.py [options]
Notes:         Requires Python 3.8+
==============================================================================
"""

#!/usr/bin/python3
from time import sleep

import options as option


# ---------------------------- Function Definition ----------------------------
def start_game() -> None:
    print("Hello, Welcome to Guessquest!")
    name = input("I'm Henry! What's Your Name? ")
    sleep(1)

    print(f"Okay, {name}. Let's Begin Guessquest!")
    print(
        "Choose a level:",
        "1. Easy",
        "2. Medium",
        "3. Hard",
        sep="\n",
    )
    sleep(1)
    try:
        level = int(input("Pick a number: "))
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
        print("ERROR! Invalid value! Please try again.\n")
        start_game()
