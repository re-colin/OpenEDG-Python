x = lambda i: i + 10

def f(x):
    return lambda x: x > 10 | x % 2

a = f(2)
print(a(3))

def f(x):
    return lambda a: int((x > 10) + (x % a))

a = f(2)
print(a(3))

a = f(2)
print(a(2))

# Numbers from 0 to 8
numbers = [i for i in range(9)]

apply_func = lambda x: x >= 5

# Filter each item in numbers by applying apply_func to each.

odds = list(filter(apply_func, numbers))
print(odds)