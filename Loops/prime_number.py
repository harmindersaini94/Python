num = int(input("Enter a number: "))
if_prime = True

for n in range(2, num):
    if num % n == 0:
        if_prime = False
        break

print(if_prime)