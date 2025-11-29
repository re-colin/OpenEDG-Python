class DoPrimes():
    def __init__(self):
        __primes = []

make_primes = lambda i: i * 2

for i in range(5):
    print(i)

def make_primes(ext):
    # primes = [ i + 1 for i in range(ext)  ]

    primes = lambda i: i + 1

    return primes

l = make_primes(5)
print(l(8))


## Iterators: a list.
class ClassList():
    def __init__(self): # first element is 0
        self.items = [ 1, 5, 3, 2, 7 ]
        self.i = 0

    def __iter__(self):
        return self 

    def __next__(self):
        if i == len(self.items):
            raise StopIteration

        self.i += 1
        print(i)


for i in ClassList():
    print(i)


