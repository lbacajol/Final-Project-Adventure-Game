# Leslie Bacajol
# Chapter 1

import Chapter1
import Chapter2

def ch1(inventory):
    print("`````Chapter 1`````")
    print("Welcome Only player!")
    start = input("Are you ready to start? yes or no?")
    if start.lower().strip() == "yes":
        answer = input("Now you have to decide to either research or explore").lower().strip()  # Player makes a choice
        if answer == "research":  # first choice
            print("Lets find something at the now for real quiet library")
            # calls to start chapter 1 again to choose a different choice
            Chapter1.ch1(inventory)

        if answer == "explore":  # second choice
            choice_1 = input("Should we keep looking close or go further?").lower().strip()  # Player makes a choice
            if choice_1 == "close":
                print("You have gain supplies!")
                inventory.append('food')  # adds food supply to list if chosen
                print("These are your supplies:", inventory)
                Chapter2.ch2(inventory)  # starts second chapter
            if choice_1 == "further":
                print("Dive into the next step")
                Chapter2.ch2(inventory)  # starts second chapter
    elif start == "no":  # second option first questions, game ends if chosen
        print("Let's try later then")
