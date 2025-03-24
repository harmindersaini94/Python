user_size = input("Enter the size of the coffee you want: "
"1. Small\n"
"2. Medium\n"
"3. Large\n")

user_shot = input("Do you want an Extra Expresso Shot: "
"1. Yes\n"
"2. No\n")

if user_shot == "Yes":
    print("Your final Order: " + user_size + " coffee with an extra expresso shot.")
else:    
    print("Your final Order: " + user_size + " coffee.")

    