str = "harminder"
rev_str = ""

for c in str:
    rev_str = c + rev_str

print("Method 1: ", rev_str)

# using Negative Indexing
rev_str = ""

for i in range(1, len(str)+1):
    rev_str = rev_str + str[-i]

print("Method 2: ", rev_str)

