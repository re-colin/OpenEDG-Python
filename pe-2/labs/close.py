# Closures are *nested functions*.
# Allow function remmber values from environment it was created in, even if said environment no longer exists.
# Often used in functional programming where you need to retain state without using global variables.
# Inner function references variables from outer function.
# Outer function returns the inner function.

def outside(x):
    def inside(y):
        return x * y
    return inside

# Creating closure with x = 4
closure = outside(4)

print(closure(3))

closure = outside(6)
print(closure(4))