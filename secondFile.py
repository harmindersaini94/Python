from hello_world import chai

chai("Chaitanya From Hello World");

# inside the python system Folder __pycache__
# helloWorld.cpython-39.pyc means the bytecode made use of cpython version with version number 3.9
# this file and folder is usually hidden but will be visible when we import file between differnt files

# WHen python is installed, a Python VM also gets installed.
# Bytecode is low level code but not machine code, and it act as a source/input for Python VM
# Machine code means direct instruction to our machine or motherboard in 0s and 1s .

import sys # This is the library for getting system information
print(sys.platform)

import os
print(os.getcwd())

# So the importance of reload here is that whenever we made change to some file of python, we do not need to
# close the terminal or stop it to get the new changes in build. Just call this reload function, this will updae the build
from importlib import reload
reload(chai)

#Python Mutable and Immmutable
# username = "harminder"  Here "harminder is an object and this is immutable, i.e it cannot be changed", although username can have a different value,
# in that case harminder will be garbage collectible, but will still remain the same

username = "harminder" # in memory pythoin create a immutable string object of harminder and username will have its reference
username = "Saini" # here python will again create a immutable string object Saini and its reference will be assigned to username and harminder will be garbage collectible here

# List: [1,2,3]
# Tuple: (1,2,3)
# Set: {1,2,3}
# Dictionary: {1:2, 2:3, 3:4}

# Interview Question:
# Python me jo datatype hai vo variable ko nhi balki memory me jo value hai usse assign hoti hai.
# So we can say that python me variable ki koi data type nhi hoti, balki uski value/ya jisse hum object kehte hai me assign hoti hai.

# Now jo object abb kisi ko nhi asssign vo garbage collecticle ho jaate hai, but umbers or string jaise objects ko garbage collectible innediately nhi hote.
