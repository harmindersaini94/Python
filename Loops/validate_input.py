user_input = int(input("Enter a number: "))

while user_input < 0 or user_input > 10:
    print("Invalid input! Please enter a number between 0 and 10.")
    user_input = int(input("Enter a number: "))

print("You entered:", user_input)

# MEthod 2

while True:
    user_input = int(input("Enter a number: "))
    if 0 <= user_input <= 10:
        break
    print("Invalid input! Please enter a number between 0 and 10.")

