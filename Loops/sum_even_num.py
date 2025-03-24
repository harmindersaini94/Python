user_input = input("Enter a number: ")
sum = 0

try:
    num = int(user_input)

    while num > 0:
        if num % 2 == 0:
            sum += num

        num -= 1

    print(f"Sum of even numbers: {sum}")

except ValueError:
    print("Please enter a valid number")

# Second Wethod, Using For Loop

try:
    num2 = int(user_input)
    sum2 = 0

    for i in range(1, num2 + 1): # range(1, num2 + 1) is used to include the last number in the range
        if i % 2 == 0:
            sum2 += i

    print(f"Sum of even numbers using For Loop: {sum2}")
except ValueError:
    print("Please enter a valid number")