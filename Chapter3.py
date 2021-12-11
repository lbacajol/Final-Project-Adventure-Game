# Leslie Bacajol
# Chapter 3
import Chapter3
import Chapter4

def ch3(inventory):
    print("`````Chapter 3`````")
    print("Hello, Only player. So far you have gain supplies and clues !hooray!")
    start = input("Are you ready to start again? yes or no?")
    if start.lower().strip() == "yes":
        # when words have underscores on the beginning and end that means those are the word choices to input for different choices
        answer = input("Now you have to choose: _transportation_ method or keep_searching where to go").lower().strip()  # player makes a choice
        if answer == "transportation":  # first choice
            choice_3 = input("Get something closer or continue_looking?").lower().strip()
            if choice_3 == "closer":
                print("Great choice to settle with!")
                inventory.append('SUV')  # adds SUV supply if chosen
                print("These are your supplies:", inventory)  # shows supply list gather
                # calls chapter 4
                Chapter4.ch4(inventory)

            if choice_3 == "continue_looking":
                print("There are many choices around")  # if chosen it starts chapter 3 again to select a different choice
                Chapter3.ch3(inventory)

        if answer == "keep_searching":  # second choice
            choice_4 = input("Choose a: place or just get traveling_guides").lower().strip()  # player makes a choice
            if choice_4 == "place":  # choice sends them to next chapter
                print("Let's head out there!")

                # call chapter 4
                Chapter4.ch4(inventory)

            if choice_4 == "traveling_guides":  # choice calls chapter 3 again to select a different choice
                print("Lets continue looking and check traveling guides")

                Chapter3.ch3(inventory)

    elif start == "no":  # second choice on the starting question, if chosen it ends the game
        print("Let's try later then")
