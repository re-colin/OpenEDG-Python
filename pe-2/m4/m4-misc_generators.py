# MODULE 4
# GENERATORS, ITERATORS CLOSURES
# FILE-SYSTEM, DIRECTORY TREE, FILES
# PYTHON STD LIBRARY MODULES

# ==========================
# Generators
# A type of iterator.

# e.g range(). 
# is a generator, thus an iterator.
# generators return a *series* of values, and are implicitly invoked more than once. 
# Here, range() generator is invoked six times, providing five values, then signalling completion.
for i in range(5):
    print(i)

# The way in which objects should behave in the context of *for* and *in* statements is the iterator protocol.
# Iterators must have two methods:
# __iter__() return the object itself, invoked once.
# __next__() returns the next value of the desired series. When there are no more values, method raises StopIteration exception.
# https://edube.org/learn/pe-2/generators-and-closures-43

class Fib:
    def __init__(self, nn):
        print("__init__")
        self.__n = nn  # length of sequence (input number)
        self.__i = 0  # current index
        self.__p1 = self.__p2 = 1 # prev two numbers in sequence

    def __iter__(self):
        print("__iter__")
        return self # returns iterator object

    def __next__(self): # invoked eleven times. 11th time terminates iteration.
        print("__next__")				
        self.__i += 1
        if self.__i > self.__n:  # once i is past our sequence length, stop
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret
    

