str = "ppyyggsehh"
found = ""

for c in str:
    if str.count(c) == 1:
        found = c
        break
    
if found != "":
    print("First unique character : ", found)
else: print("No unique character found.")

