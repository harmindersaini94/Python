# This way is also good, but here we are returning a List, but we should return num one by one
def Yield_Generator(num):
    even_num = []

    for i in range(2, num+1):
        if i % 2 == 0:
            even_num.append(i)
    
    return even_num



user_num = int(input("Enter a limit: "))

# Our task is to find even numbers uptil that point
print(Yield_Generator(user_num))

#Mathod 2 - Yield Concept

def even_num(num):
    even_num = []
    for i in range(2, num+1):
        if i % 2 == 0:
            yield i  # yha agar hum return krenge toh loop khatam ho jayega and we will only get 1 number.
            # yield yha kya krta hai ki it consumes our content and also take care of the current standing. Like yield here return the value from this function
            # which gets printed, but also keep track of the way and moves the control back to the next iteraion of the llo

for num in even_num(10):
    print(num)