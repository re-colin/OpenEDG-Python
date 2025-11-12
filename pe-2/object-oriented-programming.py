# MODULE 2 PART 3
# =====================================================================


# PROCEDURAL VS OBJECT APPROACH
# =====================================================================
# Over the decades, procedural programming was dominant software approach.
# For large and complex projects, it doesn't always work. 
# The object approach is still quite young.
# Python is universal for both object and procedural.

# Procedural distinguishes between code and data. 
#  Functions can use data, but data cant use functions. In addition, functions are free to abuse data.

# *Methods* - data that can use functions - invoked from within the data, not beside it.
# In the OOP approach, data and code are enclosed together, divided into classes.

# Classes are essentially recipes that can be used when you want to create a useful object.
# Each class has a set of traits (properties/attributes)
# Can perform a set of activities (methods)

# Properly constructed classes are able to protect its data and hide it from unauthorized modifications.

# Classes essentially form a hierarchy. Superclasses are more general/abstract, its subclasses are more specialized.

# Inheritance 
# Objects bound to a specific level of a class hierarchy inherits all traits defined inside any superclasses.
# They work as modelling specific parts of reality.

class SimplestClass:
    pass

# Instantiating and storing a class
simple_object = SimplestClass()

# STACKS 
# =====================================================================

# Last-in First-out data structure.
# Procedural approach
stack = []

def push(val):
    stack.append(val)


def pop():
    val = stack[-1]
    del stack[-1]
    return val

push(3)
push(2)
push(1)

print(pop())
print(pop())
print(pop())

# This works, but has weaknesses.
# 1. Anyone can modify it (accidentally or not), destroying the structure entirely.
# 2. You may need more than one stack or more functions - requiring seperate stack implementation.

# Stack - Object approach
# Encapsulation:
# __init__ function is ran implicitly. 
# Class components prefixed with '__' become private thus only visible from within the class.
# An AttributeError will be raised here.
class Stack:
    def __init__(self):
        self.__stack_list = []

stack = Stack()
# print(len(stack.__stack_list))

## Complete stack class.
class Stack:
    def __init__(self):
        self.__stack_list = []


    def push(self, val):
        self.__stack_list.append(val)


    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


stack = Stack()

stack.push(3)
stack.push(2)
stack.push(1)

print(stack.pop())
print(stack.pop())
print(stack.pop())
# 'self' argument is required, allowing the method to access properties/methods carried out by the object. Everytime Python invokes a method, it implicitly sends the current object as the first arg.

stack1 = Stack()
stack2 = Stack()

stack1.push(2)
stack1.push(7)
stack1.push(3)

stack2.push(2)
stack2.push(7)
stack2.push(2)

print(stack1)
print(stack2)