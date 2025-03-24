numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
count_po = 0
count_ne = 0

for num in numbers:
    if num > 0:
        count_po += 1
    elif num < 0:
        count_ne += 1

print(f"Positive numbers: {count_po}")
print(f"Negative numbers: {count_ne}")