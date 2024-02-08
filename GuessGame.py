user_name = input("What's your name? : ")
print()
# Prints a blank line to break up the text and make it more readable
print("Hi {}! This is a guessing game! Please guess the number between 1-100. You have 10 attempts!".format(user_name))
print()
guesses_left = 10
answer = 69
number = int(input(f"Guess the Number! :"))
mode = guesses_left
count = number
while guesses_left:
    if answer != number:
        if count == mode:
            guesses_left = False
            print("Sorry! Your still couldn't get it after", count, "tries!")
        elif answer < number:
            answer = int(input("That's too low!\n Try again! :"))
        else:
            answer = int(input("That's too high!\n Try again! :"))
    else:
        print("You got it in", count, "guesses! Well done!")
