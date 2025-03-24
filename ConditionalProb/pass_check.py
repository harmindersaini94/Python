user_password = input("Enter your password: ")

length = len(user_password)
if length < 6:
    print("Password is Weak")
elif length <10:
    print("Password is Medium")
else:   print("Password is Strong")