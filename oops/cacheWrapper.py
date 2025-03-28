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

'''
Explanation of How it is working, According to me , by calling DatabaseCall again and again, it
calls the Decorator Function again and again, so the cache_values must re-initialized each time

Here is the concept

Turns out that the cache_values only once when dictionary is created when the Cache decorator is called
The decorator function is only called once when the function is defined, not when it is called
its the Wraper function that replaced the original function and is called each time the function

Key Concept: Function Closures and Decorators
In Python, when a function is decorated, the decorator function is executed once at the time of decoration, and the resulting wrapped function replaces the original function.

What Happens in Your Code?
The Cache decorator is applied to DatabaseCall:

@Cache
def DatabaseCall(a, b):
This means DatabaseCall is wrapped inside wrapper, and cache_values is created once when the decorator runs.

Cache(func) executes once, and inside it:

cache_values = {} is created once.

wrapper function is returned and replaces DatabaseCall.

When you call DatabaseCall(1,2), it actually calls wrapper(1,2):

Since (1,2) is not in cache_values, it computes a + b, stores it in cache_values, and returns the result.

When you call DatabaseCall(1,2) again:

The same wrapper function runs.

Now, (1,2) is already in cache_values, so it returns the cached value instead of recomputing.

cache_values persists because it is part of the closure of wrapper, meaning it is stored along with wrapper and does not get reinitialized every function call.

Your Confusion: "Shouldn't cache_values reset every call?"
No, because cache_values is defined in the outer function (Cache), and it persists inside wrapper.

It is not reinitialized on every function call—only when the decorator runs.

Key Takeaway
The decorator runs once at the time of decoration, and the wrapped function (wrapper) retains cache_values in its closure, allowing it to remember previous results.
'''