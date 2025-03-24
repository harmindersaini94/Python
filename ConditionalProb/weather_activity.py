user_weather = input("Enter the weather: ") 

try:
    weather = str(user_weather)
    if weather == "Sunny":
        print("Go for a Walk")
    elif weather == "Rainy":
        print("Read a book")
    elif weather == "Snowy":
        print("Build a snowman")
    else:
        print("Invalid input")
except ValueError:  
    print("Invalid input")