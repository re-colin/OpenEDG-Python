# Useful standard modules
# Python Module index: https://docs.python.org/3/py-modindex.html.
# ========================================

# dir()
import math 

# Getting all functions within a package.
for name in dir(math):
    print(name, end="\t")


# math()
# ========================================
## Trigonometry
# from math import sin, cos, tan
# from math import asin, acos, atan
# sin(20)
# cos(20)
# tan(90)

# asin(45)
# acos(45)
# atan(45)

# Operations on angles
from math import pi, radians, degrees
x = 20

print(pi)
# Degrees to radians conversion
print(radians(x))

# Radians to degrees
print(degrees(x))

# Exponentiation
from math import e, exp, log, log10, log2

y = 2
z = 5
print(e)
exp(y)
log(y)
log(y,z)
log10(y)
log2(y)
pow(y,z)


# random()
# ========================================
from random import random, seed

# Seed sets the same generation of values
seed(10)
for i in range(5):
    print(random())

from random import randrange, randint

print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))

# range(beg, end, step) is equivalent to randrange(left, right+1) 


# platform()
# ========================================

from platform import platform 

print(platform())
print(platform(1))
print(platform(aliased=0, terse=1)) 
# aliased when true presents alternative underlying layer names instead of common ones
# terse may convince the function to present a briefer form of the result if possible

from platform import machine, processor, system, version

print(machine()) # Generic processor name e.g x86_64

print(processor()) # Real processor name

print(system()) # Generic OS name 

print(version()) # OS Version

# Platform Python implementations
from platform import python_implementation, python_version_tuple

print(python_implementation()) # Python implementation (CPython, unless non-canonical branch used)

# major.minor.patch level
for atr in python_version_tuple():
    print(atr)


