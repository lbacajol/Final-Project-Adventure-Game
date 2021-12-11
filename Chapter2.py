# Leslie Bacajol
# Chapter 2

import Chapter2
import Chapter3

def ch2(inventory):
    print("`````Chapter 2`````")
    print("Welcome back Only player!")
    start = input("Are you ready to start again? yes or no?")
    if start.lower().strip() == "yes":
        # when words have underscores on the beginning and end that means those are the word choices to input for different choices
        answer = input("Now you have to decide to either: gather_supplies or explore_town").lower().strip()  # Player makes a choice
        if answer == "gather_supplies":  # first choice
            choice = input("Go to different: stores? or move_on?").lower().strip()
            if choice == "stores":  # this choice calls beginning of chapter 2 again to choose something else
                print("Keep getting stuff!")
                Chapter2.ch2(inventory)
            if choice == "move_on":  # this choice sends them to next chapter
                print("Let's dive to the next steps")

                # start ch3 here
                Chapter3.ch3(inventory)

        if answer == "explore_town":  # second choice
            explore = input("Explore buildings: local? or move_on?").lower().strip()  # Player makes a choice
            if explore == "local":
                print("You have gain new supplies!")
                inventory.append('tools')  # adds tools supply to list if chosen
                print("These are your supplies:", inventory)
                Chapter3.ch3(inventory)  # starts 3rd chapter
            if explore == "move_on":
                print("Dive into the next step")
                Chapter3.ch3(inventory)  # starts 3rd chapter


    elif start == "no":   # second option entry question to start game, if chosen it ends the game
        print("Let's try later then")
