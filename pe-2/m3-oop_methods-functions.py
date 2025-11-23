# Methods are functions embedded within classes.
# Must have self parameter included.
# Other methods can be invoked from inside the class using self.
class Stack():
    def __init__(self):
        self.__stack = []
    
    def push(self, val):
        self.__stack.append(val)

    def pop(self):
        del self.__stack[-1]

    def show_stack(self):
        return self.__stack

    # Hidden/private function.
    def __show_stack_size(self):
        return len(self.__stack)

# Instance variables
s1 = Stack()
s1.push(2)
s1.push(3)
s1.push(7)

try: 
    print(s1.stack)
except AttributeError:
    print("s1.stack variable private to Stack.")

# Function to provide 'read' access to a private variable.
print(s1.show_stack())  # [2,3,7]

# __dict__ is a built-in Python variable for accessing all names and values of an object or a class.
# Different values are shown for accessing either the class or a class instance/object.
# For a *class*, it shows all of its data such as module, memory locations of its variables, and its functions and attributes.
print(Stack.__dict__)

# Accessing the dict of our instance returns the data initialized by the constructor. In this case stack_list within __init__.
print(s1.__dict__)

# Alternatively, to check if a class or class instance/object has a certain variable, hasattr() is a more elegant solution than using a try-except block.
# It will also return False if the variable being accessed is private.
print(hasattr(Stack, "__stack"))

# For private variables, their variable names are automatically changed.
# print(_Stack__show_stack_size())

# __module__ stores the name of the file containing the definition of the class - the one currently being run.

# Finding the class of a particular class instance/object.
print(type(s1).__name__)

# __bases__ returns a tuple containing classes which are direct superclasses for the class.
# Only classes have this attribute. Objects do not.
# A class without an explicit superclass points to a predefined class called *object*.
print(Stack.__bases__)

print(s1) # Hex memory address e.g <__main__.Classy object at 0x00000247103A3B50>

print(s1.__str__) # <method-wrapper '__str__' of Classy object at 0x000001B516413B50>

# 'is' checks whether two variables refer to the same object.
# Variables dont store objects themselves, only the handles pointing to their memory location.
# Assigning the value of an object variable to another doesnt copy the object; only its handle.
stack1 = Stack()
stack2 = Stack()
stack3 = stack1
print(stack3 is stack1) # True
print(stack1 is stack3) # True
print(stack1 is stack2) # False
# Not to be confused with the is equal (==) operator which checks if two *values* are the same.

