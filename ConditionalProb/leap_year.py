user_year = input("Enter a year: ")

try:
    year = int(user_year)
    if year % 100 == 0 and year % 400 == 0:
        print("Leap year")
    elif year % 4 == 0 and year % 100 != 0:
        print("Leap year")
    else:
        print("Not a Leap year")


except ValueError:
    print("Please enter a valid year.")