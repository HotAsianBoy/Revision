def integer_checker(question):
    error = "\nSorry, you must enter an integer\n"
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print(error)


total = 0


first_integer = integer_checker("Enter the first integer: ")
second_integer = integer_checker("Enter the second integer: ")


if first_integer < second_integer:
    for number in range(first_integer, second_integer + 1):

        sub_total = total + number
        print(f"{number} added to {total} = {sub_total}")
        total = sub_total
else:
    for number in range(second_integer, first_integer + 1):

        sub_total = total - number
        print(f"{number} subtracted to {total} = {sub_total}")
        total = sub_total

