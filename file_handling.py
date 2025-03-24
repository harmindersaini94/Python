# To open a file, Python has a built-in function open().

fs = open('sample.py')

# Now here Fs has the file contens of sample.py. Now we can make use of readline() function to read the file line by line.

print(fs.readline()) # This readline is a iterator tool, meaning, like here we did readline(), it read Line 1
# Now we again do readline(), it will read Line 2 and so on.
print(fs.readline())
print(fs.readline())
print(fs.readline())

fs.close() # Make sure to close the file after reading it.

# We can make use of For loop  here as well

for line in open('sample.py'):
    print(line, end='') # end='' is used to remove the extra line space that is added by print function.

fs.close()  

# Using While Loop
while True:
    line = fs.readline()
    if not line:  # Here this syntax checks if line is emoty or not, empty or "" ,measn False, so it will break the loop.
        break
    print(line, end='')
fs.close()  