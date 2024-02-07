"""First part of a program which sets up a simple True/False game
Created by Gideon Wong
Version 1
"""
user_name = input("What's your name?: ")
print() # Prints a blank line to break up the text and make it more readable
print("Hi {}! This is a game of True or False.".format(user_name))
print()
# Used \n to split the line below this (Too much text for one line!)
user_answer = input("The Earth is closer to the sun in summer than winter."
                    "\nPlease answer \"T\" for True OR \"F\" for False:")
print()
if user_answer == "F":
    print("Yes, that's right!")

else: # Used \n to split the line below this for the same reason
    print("Sorry, that's wrong. The Earth's distance from the sun does not\n"
          "determine the seasons.")


