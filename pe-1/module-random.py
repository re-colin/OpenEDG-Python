import random

for i in range(0, 10):
    print(random.randint(1,10))  # From 1 to 10 (inclusive)

print("==================")

for i in range(0, 10):
    print(random.randrange(1,10)) # from 1 to 9 

print("==================")

for i in range(0, 10):
    print(random.randrange(1, 10, 4))  

print("==================")

from random import randrange

lottoNumber = random.randrange(1,10)

print(lottoNumber)

print("==================")

# from random import *

# print(randint(1,5))
# print(random.randint(1,5))

print("==================")

from random import randrange

lotto = random.randrange(1, 10)
print(lotto)


