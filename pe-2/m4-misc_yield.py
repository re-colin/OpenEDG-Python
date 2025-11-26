# MODULE 4
# Yield

# Inconvenience - needing to save state of the iteration (e.g, fib iterator had to store exactly where last invoke stopped) between subsequent __iter__ invokes.

# *Generators* essentially save the state of the function each iteration.
def fun(n):
    for i in range(n):
        yield i

# A generator isnt a function. its its own thing, and cant be invoked explicitly like a function would.
# Doing so would return the identifier, not the series.
for v in fun(5):
    print(v) 

# e.g 2
def power_2(n):
    powr = 1

    for i in range(n):
        yield powr
        powr *= 2

for p in power_2(5):
    print(p)

# ===========================================
# List Comprehension
# list() function lets you transform a series of generator invokes into a list.
# in, not in operations are allowed as a result like normal.
pows = list(power_2(8))
print(pows)

# See fibonacci generator using yield as opposed to the object method.
l = [2 ** pw for pw in range(10)]
print(l)

# Conditional expressions based on boolean expression result.
# Not a conditional instruction. Tis an operator.
l = []

for i in range(10):
    l.append(i if i % 2 == 0 else 0)

print(l)

# Alternatively,
l = [l if l % 2 == 0 else 0 for l in range(10)]
print(l)

# ===========================================
# Generators as list comprehensions
# Parenthesis instead of square brackets makes it a generator instead of a list.
# In the list method, an actual list is being created.
# Here, we are only getting a sequence of values through our generator.
g = (i if i % 2 == 0 else 0 for i in range(10))

for v in g:
    print(v, end=" ") # 

