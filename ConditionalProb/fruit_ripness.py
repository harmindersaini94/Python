user_input = input("Enter the ripeness of the fruit: ")

try:
    ripeness = str(user_input)
    if ripeness == "Green":
        print("The fruit is unripe")
    elif ripeness == "Yellow":
        print("The fruit is ripe")
    elif ripeness == "Brown":
        print("The fruit is overripe")
    else:
        print("Invalid input")

except ValueError:
    print("Invalid input")