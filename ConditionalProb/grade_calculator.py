user_score = input("Enter your score: ")

try:
    #try block here
    score = float(user_score)
    if score > 100:
        print("Invalid Score, Please enter again")
        exit()


    if score < 60:
        print("F")
    elif score <70:
        print("D")
    elif score <80:
        print("C")
    elif score <90:
        print("B")
    elif score <=100:
        print("A")
except ValueError:
    print("Invalid input")

"""
Here in the above program, we are using a general except block that catches all type of exception
When the exit() function is called, it raise a SystemExit exception, that is why it gets caught as well

A way to resolve this is to define the type of exception that we want to catch, like ValueError exception that 
we want here

Another way is to make use of return statement instead of exit() function but for that we have to put the code inside a
function, because return statement can only be used inside a function

Another way is to use break, but that only works inside a loop
"""