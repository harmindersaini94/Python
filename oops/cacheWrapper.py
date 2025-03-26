# This code here will keep track of the result and will return them in case we already have them
# Just like memoization

import time

# Hmesha Decorator bnate time pehle jo parameter me function hai uska kaam kro, uske baad addition functionaity kro
def Cache(func):
    cache_values = {} # why dict, coz it is easy to search in dict
    print("Cache Values: ",cache_values)
    def wrapper(*args):
        if args in cache_values:
            return cache_values[args]
        
        result = func(*args)
        cache_values[args] = result
        return result
    return wrapper

@Cache
def DatabaseCall(a,b):
    time.sleep(4) # This is done to simulate a database call
    return a+b

print(DatabaseCall(1,2))
print(DatabaseCall(1,2))
print(DatabaseCall(3,2))