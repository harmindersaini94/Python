user_age = input("Enter your age: ")

try:
    age = int(user_age)
    if age < 13:
        print("You are a Child")
    elif age >= 13 and age <= 19:
            print("You are a Teenager")
    elif age >= 20 and age <= 59:
            print("You are a Adult")
    elif age >= 60:
            print("You are a Senior Citizen")
        
except:
    print("Please enter a valid number")