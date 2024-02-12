def number_checker(question):
    error = "\nSorry, you must enter a valid number please!\n"
    number = ""
    while not number:
        try:
            number = float(input(question))
            return number
        except ValueError:
            print(error)


daily_volume = 0.0
commercial_factor = 0.5
residential_factor = 0.25


while True:
    building_type = input("What type of building is this? \nEnter 'C' for "
                          "commercial and 'R' for residential"
                          " or 'X' to exit!: ").upper()
    if building_type == "X":
        break
    else:
        while building_type != "C" and building_type != "R":
            building_type = input("Please enter a valid building type! \nEnter "
                                  "'C' for commercial or 'R' for residential "
                                  "or 'X' for exit!: ").upper()
    foundation_length = number_checker("Enter the length of the required "
                                       "slab - in meters!: ")
    foundation_width = number_checker("Enter the width of the required "
                                      "slab - in meters!: ")
    area = foundation_length * foundation_width
    if building_type == "C":
        required_volume = area * commercial_factor
    else:
        required_volume = area * residential_factor

    required_volume = round(required_volume, 2)
    print(f"The volume of concrete needed for this building is "
          f" {required_volume} cubic meters!\n")
    daily_volume += required_volume
    break

print(f"\nThe total volume of concrete required today will be {daily_volume} "
      f"cubic meters!")
print()
print("Farewell!")
