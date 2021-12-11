# Leslie Bacajol
# Chapter 4

import Chapter4
import Chapter5

def ch4(inventory):
    print("`````Chapter 4`````")
    print("Welcome to the journey Only player")
    start = input("Are you ready to start again? yes or no?")
    if start.lower().strip() == "yes":
        # when words have underscores on the beginning and end that means those are the word choices to input for different choices
        answer = input("What would you do? _stop_ and continue exploring different places, keep looking for _clues_ or just leave _signals_?").lower().strip()  # player makes a choice
        if answer == "stop":  # first choice, goes to next chapter
            print("Lets explore this scenarios but continue the journey")
            # call chapter 5
            Chapter5.ch5(inventory)

        if answer == "signals":  # second choice, adds supply, goes to next chapter
            print("Great signal! lets carry on")
            inventory.append('signal')  # adds signal supply if chosen
            print("These are your supplies:", inventory)  # shows supplies list gather
            # calls chapter 5
            Chapter5.ch5(inventory)

        if answer == "clues":  # third option
            choice_4 = input("Get and leave research or settle?").lower().strip()
            if choice_4 == "research":  # first option, goes to next chapter
                print("Great choice to carry on!")
                # calls chapter 5
                Chapter5.ch5(inventory)

            if choice_4 == "settle":  # second option, calls for chapter 4 to start again to select a different choice
                print("Let's continue look around")
                Chapter4.ch4(inventory)

    elif start == "no":  # second option first question, if chosen ends the game
        print("Let's try later then")
