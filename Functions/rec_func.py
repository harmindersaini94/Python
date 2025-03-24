def rec(num):
    if num == 0 or num == 1:
        return 1
    else: return num * rec(num-1)


print(rec(5))