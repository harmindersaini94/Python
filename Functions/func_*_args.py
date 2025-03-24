def sum_all(*args): # the standard name for this is *args but we can use any name, but * is necessary
    return sum(args) # sum() is a built-in function that takes an iterable and returns the sum of all the elements

print(sum_all(1, 2, 3, 4, 5))  # 15
print(sum_all(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))  # 55
