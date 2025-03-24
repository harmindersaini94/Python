items = ["apple", "banana", "orange", "apple", "mango"]

for item in items:
    if items.count(item) > 1:
        print(item)
        break

# Method 2

unique_item = set()

for item in items:
    if item in unique_item:
        print(item)
        break
    else: unique_item.add(item)