# MODULE 4
# Lambda Functions

# lambda parameters: expression
# Can be assigned to variables and called upon.
# Unlike normal functions where their return value is stored within the variable.
pwr = lambda x, y: x ** y

print(pwr(2,3))

# Lambdas are anonymous parts of code intended to evaluate a result.
# Good for when you only need to evaluate an expression one time.

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