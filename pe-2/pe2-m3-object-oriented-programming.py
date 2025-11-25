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
    __d = 4
    e = 5
    def __init__(self, val):
        c = 2
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass(1)

print(example_object.a)
# print(example_object.b) # AttributeError

# hasattr() is more elegant than using a try/except block to see if a class has an attribute or is available to use.
# c accessible only when instantiated.
print(hasattr(example_object, 'c'))
print(hasattr(ExampleClass, 'c'))

# a accessible only when instantiated/__init__ function runs successfully and creates variable.
print(hasattr(ExampleClass, 'a'))
print(hasattr(example_object, 'a'))

# d inaccessible, private variable
print(hasattr(ExampleClass, 'd'))
print(hasattr(example_object, 'd'))

# e is a set global variable constant in all classes/their instances.
print(hasattr(ExampleClass, 'e'))
print(hasattr(example_object, 'e'))

## =======================================================
# METHODS
# Functions embedded inside classes.
# Must have atleast one parameter (self)
# Other methods can be invoked from inside the class using 'self'.
class Classy():
    varia = 1
    def __init__(self):
        self.var = 2

    def other(self):
        print("other method")

    def method(self, val):
        print("method: ", val)
        self.other()

    def __hidden(self):
        print("hidden")


obj = Classy()
obj.method(3)
obj.method(2)
obj.method(1)
obj._Classy__hidden() # Mangling in order to use a private method or variable

print(obj.__dict__, "\n") # Data assigned in __init__ constructor (context: object)
print(Classy.__dict__)    # Everything else (context: class)
print(Classy.__name__)    # __name__ is simply the name of the class. Doesnt exist in objects, only classes. 

# If you'd like to find the class of a particular object
print(type(obj).__name__)

# __module__ Stores the name of the module containing the definition of a class.
# __module__ is the file currently being run.
print(Classy.__module__) # __main__
print(obj.__module__) # __main__

# __bases__ returns a tuple containing classes which are direct superclasses for the class.
# Only classes have this attribute. Objects do not.
# A class without an explicit superclass points to a predefined class called *object*.
print(Classy.__bases__) # (<class 'object'>,)
print(AddingStack.__bases__) # (<class '__main__.Stack'>,)

# Python programmers as a result can perform:
# Introspection > Ability of a program to examine the type or properties of an object at runtime
# Reflection > Ability of a program to manipulate the values, properties and functions of an object at runtime
# So its not required that you know the complete class/object definition to manipulate said object.

# =========================================================
# INHERITANCE

print(obj) # Hex memory address e.g <__main__.Classy object at 0x00000247103A3B50>

print(obj.__str__) # <method-wrapper '__str__' of Classy object at 0x000001B516413B50>

# Checking if a class is a subclass of another.
# Classes are considered to be subclasses of themselves.
print(issubclass(AddingStack, Stack))
print(issubclass(Stack, Stack))

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

# super() function
# Creates a context where you dont have to/can't pass the self argument to the method being invoked, activating the superclass constructor with only one argument.
class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."


class Sub(Super):
    def __init__(self, name):
        super().__init__(name)


obj = Sub("Taft")
print(obj)
# Not only can you invoke the superclass constructor with it, but also get access to any resources available within the superclass.
# Testing properties: class variables.
class Super:
    supVar = 1
    def __init__(self):
        self.supVar2 = 11


class Sub(Super):
    subVar = 2
    def __init__(self):
        super().__init__()
        self.subVar2 = 13

obj = Sub()

# Superclass variable accessed from subclass object. Both are visible from the subclass.
print(obj.subVar)
print(obj.supVar)
# Instance variables accessible through subclass.
# Must call superclass init function / Superclass constructor invocation.
print(obj.subVar2)
print(obj.supVar2)

# ============================================================================
# How Python finds properties and methods: Continued
# When trying to find any objects entity, python will:
# 1. find it inside the object itself
# 2. find it in all classes involved in the objects inheritance, from bottom to top
# if both fail, attributeerror is raised
# When a subclass has exactly one superclass (single inheritance). The most common and most recommended situation.

# Multiple inheritance occurs when a class has more than one superclass.
 
# OVERRIDING:
# Level 2 is a subclass of Level1. It overrides its var variable and fun() method.
class Level1:
    var = 100
    def fun(self):
        return 101


class Level2(Level1):
    var = 200
    def fun(self):
        return 201


class Level3(Level2):
    pass


obj = Level3()

print(obj.var, obj.fun())

# ==============================================

class Left:
    var = "L"
    var_left = "LL"
    def fun(self):
        return "Left"


class Right:
    var = "R"
    var_right = "RR"
    def fun(self):
        return "Right"

# Additionally, if theres more than one class on an inheritance path, Python scans them from left to right.
# Sub(Right, Left) -> R LL RR Right
class Sub(Left, Right): # -> L LL RR Left
    pass


obj = Sub()

print(obj.var, obj.var_left, obj.var_right, obj.fun())

# ==============================================
# Building a hierarchy of classes: Polymorphism
# Where a subclass is able to modify its superclass behaviour.
# Showcase of how Python searches for objects - bottom to top.
# Each call of the doanything() function invokes the first occurance of its definition as Python scans for it - When two.doanything() is called, Two() searches in its superclass, and finds the first occurance of doanything() referring to itself - class Two.
class One:
    def do_it(self):
        print("do_it from One")

    def doanything(self):
        self.do_it()


class Two(One):
    def do_it(self):
        print("do_it from Two")


one = One()
two = Two()

one.doanything()
two.doanything()

# Polymorphism as extending class flexibility
# Building a class hierarchy for specialisation.

# This code's commented lines error for some reason.
# The point is that by changing the Vehicle's turn method, the rest of the subclasses will inherit the change. One change and the rest will still follow it.
import time

class Vehicle:
    def change_direction(left, on):
        pass

    def turn(left):
        # change_direction(left, True)
        time.sleep(0.25)
        # change_direction(left, False)


class TrackedVehicle(Vehicle):
    def control_track(left, stop):
        pass

    def change_direction(left, on):
        # control_track(left, on)
        pass


class WheeledVehicle(Vehicle):
    def turn_front_wheels(left, on):
        pass

    def change_direction(left, on):
        # turn_front_wheels(left, on)
        pass


# ============================================================
# COMPOSITION
# Composing an object using other, different objects.
# Inheritance extends a class's capabilities by adding new components/modifying existing ones. Complete recipe is contained inside the class and its ancestors. The object takes all the classes' belongings and makes use of them.
# Composition projects a class as a container able to store and use other objects derived from other classes. Each part makes up the whole.

import time

class Tracks:
    def change_direction(self, left, on):
        print("tracks: ", left, on)


class Wheels:
    def change_direction(self, left, on):
        print("wheels: ", left, on)


class Vehicle:
    def __init__(self, controller):
        self.controller = controller

    def turn(self, left):
        self.controller.change_direction(left, True)
        time.sleep(0.25)
        self.controller.change_direction(left, False)

# New vehicle types are crafted from Wheels and Tracks classes.
wheeled = Vehicle(Wheels())
tracked = Vehicle(Tracks())

wheeled.turn(True)
tracked.turn(False)

