user_num = input("Enter a number: ")

try:
    num = int(user_num)

    for i in range(1, 11):
        if i != 5:
            print(str(num) + " x " + str(i) + " = " + str(num * i) )

except ValueError:
    print("That's not a number.")