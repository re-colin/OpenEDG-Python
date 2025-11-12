import module

# =======================================
# When Python *first* imports a module, its contents are translated into semi-compiled Python code ready to be executed by the Python interpreter. 
# This means itll be executed faster than if it were from scratch.
# If its been modified, the pyc file will be rebuilt.
# module.cpython-311.pyc

print(module.counter)

# When files are ran directly, their __name__ variables are set to __main__.
# When a file is imported as a module, its __name__ is set to the files name.
# Use these to detect the context where a file is running in.
# Alternatively, if you have alot of functions in a module, you can use these to place a series of tests to check if said functions work the way they should. Said tests will be omitted when imported as a module.

# =======================================
# Trusting users not to use a variable from a module
# convention: preceding variable with _ or __ 
# _var, __var

# =======================================
# How Python finds modules
# Via a list called `path` - searches folders until it reaches the first folder containing the target module
# path variable is accessible through `sys` module
import sys

# The first path's element is where the execution starts
for p in sys.path:
    print(p)

# Convincing python to search a non-standard package directory
from sys import path 
path.append('C:\\Users\\cols\\python-modules\\pe-1')

for p in sys.path:
    print(p)

from cols_modules.cools.pirate import pirate
pirate()

# Importing functions from their respective directories
# cols_modules folder is in the same dir as our main.py, so we can import egg() like this
from cols_modules.cools.egg import egg
egg()

# =======================================
# Dedicated python modules and functions go in their own folders in a directory tree
# Transforming a directory tree into a module requires initialization

# __init__.py File is executed when any package modules are imported.
# If you dont want special initializations, leave it empty but not omitted.

# =======================================
# Python can also utilise .zip files to save space.

# path.append('C:\\Users\\cols\\python-modules\\pe-1\\pack.zip')

