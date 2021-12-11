# Leslie Bacajol
# Chapter 5

import Chapter5

def ch5(inventory):
    print("`````Chapter 5`````")
    print("Welcome back to the journey Only player")
    start = input("Are you ready to start again? yes or no?")
    if start.lower().strip() == "yes":
        # when words have underscores on the beginning and end that means those are the word choices to input for different choices
        answer = input("_continue_ exploring and gathering supplies? or _follow_the signal to see if there is someone else?").lower().strip()  # player makes a choice
        if answer == "continue":  # first choice
            print("Gathers more supplies and stops at camp sight")

            # calls for chapter 5 to start from the beginning for user to select a different choice
            Chapter5.ch5(inventory)

        if answer == "follow":  # second choice
            choice_5 = input("There is a camp with a fire place! Should it be: investigated or continue?").lower().strip()  # player makes a choice
            if choice_5 == "investigated":  # first outcome
                print("Continue journey! but wait could that be someone??")

                print(len(inventory), "Supplies gained throughout the journey!")  # shows the amount of supplies accumulated

            if choice_5 == "continue":  # second outcome
                print("Just carrying on with supplies and doubt")

                print(len(inventory), "Supplies gained throughout the journey!")  # shows the amount of supplies accumulated

    elif start == "no":  # second option first question, if chosen game ends
        print("Let's try later then")


