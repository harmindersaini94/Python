# Decorators matlab tool booth

# basic Syntax of a decoreator
'''
def DecMain(func):
    def wrapper(*args, **kwargs): # a,b of the add function will be passed here in args
        # Do some processing on args and kwargs
        result = func(*args, **kwargs)
        return result
    return wrapper

@DecMain
def add(a, b):
    return a + b

add(2, 3)

Now what will happen is that this add function will not execute here directly
The entire function will be passed to the DecMain function and the DecMain function will return the wrapper function
and the wrapper function will be executed instead of the add function

'''
import time

def SleepDecorator(func):
    def wrapper(*args, **kwargs):
        # Print the name of the function that calls the SleepFunction and also the duration of the sleep
        print(f"{func.__name__} has called the SeepFunction and the sleep duration is {args[0]} seconds")
        func(*args, **kwargs)
    return wrapper

@SleepDecorator
def SleepFunction(n):
    time.sleep(n)

print(SleepFunction(2))