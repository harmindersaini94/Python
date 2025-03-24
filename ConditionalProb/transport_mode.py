user_distance =  input("Enter the distance you want to travel: ")

try:
    distance = float(user_distance)
    if distance < 3:
        print("Walk")
    elif distance < 15:
        print("Bike")
    else: print("Car")
except ValueError:
    print("Invalid transport mode")