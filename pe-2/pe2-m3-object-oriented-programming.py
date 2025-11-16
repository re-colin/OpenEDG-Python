# MODULE 2 PART 3: OBJECT ORIENTED PROGRAMMING =====================================================================


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

# Constructing a subclass
class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self) # Must explicitly invoke superclass constructor - of which initializes the __stack_list property
        self.__sum = 0

    # Subclasses' overriding of its superclasses' push() function.
    # It acts as an interface for accessing the superclass function aswell as adding functions, like incrementing the __sum variable.
    def push(self, val):
        self.__sum += val 
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val 

    # Displaying a read-only function variable to the user
    def get_sum(self):
        return self.__sum
    
stack_object = AddingStack()

for i in range(5):
    stack_object.push(i)

print(stack_object.get_sum())

# =========================================================
# Instance variables
# Python objects have predefined properties and methods that you dont add. e.g a property named __dict__, containing all names and values the object is currently carrying.
# Here, we edit instance variables of multiple Example objects. These are completely isolated from eachother.

class Example:
    def __init__(self, val = 1):
        self.first = val

    def set_second(self , val = 2):
        self.second = val 


example1 = Example()
example2 = Example(2)
example2.set_second(3)

example3 = Example(4)
example3.third = 5  

print(example1.__dict__) # {'first': 1}
print(example2.__dict__) # {'first': 2, 'second': 3}
print(example3.__dict__) # {'first': 4, 'third': 5}


# Here, the same thing is done, except now our Example class it's objects are private.
# When you want to add an instance variable to an object and are going to do it inside the object's methods, the operation is mangled.
# - class name before object name
# - additional underscore at the beginning
# This mangling wont work if you add a private instance variable outside the class block - itll behave like any other property.
class Example:
    def __init__(self, val = 1):
        self.__first = val

    def set_second(self, val = 2):
        self.__second = val


example1 = Example()
example2 = Example(2)

example2.set_second(3)

example3 = Example(4)
example3.__third = 5


print(example1.__dict__) # {'_Example__first': 1} 
print(example2.__dict__) # {'_Example__first': 2, '_Example__second': 3} 
print(example3.__dict__) # {'_Example__first': 4, '__third': 5} 

# The same name is accessible from outside the class.
print(example1._Example__first) # 1

# =========================================================
# Class variables
# A property that exists in just one copy, stored outside any object.
# No instance variable exists if there is no object in the class.
# A class variable exists in one copy even if theres no objects in the class.
#  

class ExampleClass:
    counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.counter += 1


# The 'counter' variable is the same across all objects.
example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)

print(example_object_1.__dict__, example_object_1.counter)
print(example_object_2.__dict__, example_object_2.counter)
print(example_object_3.__dict__, example_object_3.counter)

# =========================================================
# Class variables 2

class ExampleClass:
    varia = 1
    def __init__(self, val):
        # Note self vs ExampleClass assignmenti
        # Changing assignment to self.varia creates an instance variable of the same name as the class's one.
        # Saying varia = val operates on the methods local variable. 
        self.varia = val # 1
        # varia = val # 1
        # ExampleClass.varia = val # 2



example_object = ExampleClass(2)

print(ExampleClass.__dict__)
print(example_object.__dict__)

# Class __dict__ variable
print(ExampleClass.__dict__) # {'__module__': '__main__', 'counter': 3, '__init__': <function ExampleClass.__init__ at 0x000001D18F0BA840>, '__dict__': <attribute '__dict__' of 'ExampleClass' objects>, '__weakref__': <attribute '__weakref__' of 'ExampleClass' objects>, '__doc__': None}

# Object __dict__ variable
print(example_object_1.__dict__) # {'_ExampleClass__first': 1}

print(ExampleClass.varia)

# =============================================
# Not all objects of the same class have the same properties.

class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass(1)

print(example_object.a)
# print(example_object.b) # AttributeError

