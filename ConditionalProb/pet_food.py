user_pet = input("What pet do you have? \n"
"1. Dog\n"
"2. Cat\n")

user_age = input("What is your pet's age?")

pet = int(user_pet)
age = int(user_age)

if pet == 1:
    if age < 2:
        print("You should feed your dog puppy food.")
    elif age >= 2:
        print("You should feed your dog adult food.")
elif pet == 2:
    if age < 2:
        print("You should feed your cat kitten food.")
    elif age >= 2:
        print("You should feed your cat adult food.")