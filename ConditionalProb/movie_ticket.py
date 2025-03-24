from datetime import datetime

user_age = input("Enter your age: ")
movie_price = 0

try:
    #try block here
    age = int(user_age)
    if age < 18:
        movie_price = 8
    else:
        movie_price = 12

# Moday = 0 ... Sunday = 6
    if datetime.now().weekday() == 2:
        movie_price = movie_price - 2

    print(f"Your ticket price is $:{movie_price}")
except:
    print("Please enter a valid number")

# Shorthand Syntax
# price  = 12 if age >= 18 else 8  --< Try to use this syntax for better readability