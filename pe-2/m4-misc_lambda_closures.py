# MODULE 4
# Lambda Functions

# lambda parameters: expression
# Can be assigned to variables and called upon.
# Unlike normal functions where their return value is stored within the variable.
pwr = lambda x, y: x ** y

print(pwr(2,3))

# Lambdas are anonymous parts of code intended to evaluate a result.
# Good for when you only need to evaluate an expression one time.

# PEP 8 says lambdas shouldnt be assigned to variables, but rather defined as functions.
def f(x): return x

# ===========================================
# map(function, list) 
# where list is any iterable.
# can accept >2 arguments.
# Applies function passed to all its second argument's elements, returning an iterator with each subsequent function result.

list_1 = [x for x in range(5)]
list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_2)

for x in map(lambda x: x * x, list_2):
    print(x, end=' ')
print()

# Lambdas and filter()
# Here, functions returned true pass the filter. others are disregarded.
from random import seed, randint

seed()
data = [randint(-10,10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

print(data)
print(filtered)

# ===========================================
# Closures
# Allows storing of values when the context theyve been created in doesnt exist anymore.
# Here, two() is accessible *only* from within one().  
# The function returned during one()'s invocation is a *closure*. 

# one() returns a copy of the two() function, the one frozen at the moment of one()'s invocation, which contains its full environment, e.g local variable state, meaning variable let is retained even though its function (one()) already ceased to exist.
def one(var):
    let = 2

    def two():
        return let
    return var 

var = 1
fun = print(one(var))

# closure with parameters
# first closure obtained from make_closure defines a tool.
# the second makes use of the argument.
# Closures make use of the frozen environment, but also *modify its behaviour* by using values from the outside.
def make_closure(var):
    let = var

    def pwr(p):
        return p ** let

    return pwr 

# Calling make_closure or printing f1/f2 as is returns the function make_closure *object*.
f1 = make_closure(2)
f2 = make_closure(3)

print(f1)
print(f2)

# To get the return value, pass the argument as a variable.
print(f1(2)) # 4
print(f2(3)) # 27

# for i in range(5):
#     print(i, f1(i), f2(i))

