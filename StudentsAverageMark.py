def number_checker(question):
    error = "\nSorry, please enter a valid number!"
    number = ""
    while not number:
        try:
            number = float(input(question))
            return number
        except ValueError:
            print(error)


total_marks = 0
marks_list = []
best_mark = 0
best_student = []


while True:
    name = input("Student name: ").title()
    if name == "X":
        break
    else:
        if len(name) < 2:
            print("A person's name must be at least 2 characters long!")
            continue
        else:
            mark = number_checker(f"{name}'s mark: ")
            while not 0 <= mark <= 100:
                print("Marks can only be between 0 and 100!")
                mark = number_checker(f"{name}'s mark: ")
            else:
                total_marks += mark
                marks_list.append([name, mark])
        break


total_students = len(marks_list)
for student in marks_list:
    if student[1] > best_mark:
        best_mark = student[1]
        best_student = [student]
    elif student[1] == best_mark:
        best_student.append(student)


average_mark = round(total_marks/total_students, 2)
print(f"\nThe average mark was {average_mark}! ")
if len(best_student) > 1:
    print("The best students are...: ")
    for student in best_student:
        print(f"\t{student[0]}")
    print(f"\t\tall with {best_student[0][1]} marks! ")
else:
    print(f"{best_student[0][1]} was the best student!, with a "
          f"mark of {best_mark}!")



print(f"\nThe full complete list is...:")
for student in marks_list:
    print(f"\t{student[0]}, with {student[1]} marks!")
