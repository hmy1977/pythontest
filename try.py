#!/usr/bin/env python

import random

def main():
    """Start a number guessing game between 1-100."""
    print("Guess the number!")

    x = random.randint(1, 100)
    print(x)
    guess = None

    while x !=guess:

        guess = int(input("Pick a number between 1 tp 100:"))

        if x == guess:
            print("You genius!")
        else:
            print("HAHAAHHAAAHA.")

main()