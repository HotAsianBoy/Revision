number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))

if number2 < number1:
    print(f"{number1} is bigger than {number2}!")
elif number2 > number1:
    print(f"{number2} is bigger than {number1}!")
elif number2 == number1:
    print("The numbers are equal!")