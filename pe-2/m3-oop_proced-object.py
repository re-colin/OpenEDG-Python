class SimplestClass:
    pass

simplest_object = SimplestClass()

# PROCEDURAL VS OBJECT APPROACH
# A very simple procedural stack with only functions and a  variable
stack = []

def push(stack, val):
    stack.append(val)

def pop(stack):
    del stack[-1]
    return stack


# OOP
# A very simple Stack object with its *own* functions and a public stack variable.
# __init__ constructor doesnt exist here.
# self keyword is an essential argument
# The stack variable here is also global. It will have the exact same data across all Stack instances.
# Big no no. Place within init function for flexiblity and verbosity.
# 'self' argument is required, allowing the method to access properties of the object. Python implicitly sends the current object as the first arg when a method is invoked.
class Stack():
    stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        del self.stack[-1]

s1 = Stack()
s1.push(2)
s1.push(3)
s1.push(7)
print(s1.__dict__)
print("s1.Stack: ", s1.stack) # can only be accessed since stack list is public.
s1.pop() 
print("s1.Stack: ", s1.stack)
 
# Stack class with init constructor and private variables.
class Stack():
    def __init__(self):
        self.__stack = []
    
    def push(self, val):
        self.__stack.append(val)

    def pop(self):
        del self.__stack[-1]

s1 = Stack()
s1.push(2)
s1.push(3)
s1.push(7)

