### MODULE 4 - Function arguments, dictionaries and tuples
### M4 Quiz q's

# tup = (1, ) + (1, )
# tup = tup + tup

# print(tup)
# print(len(tup))

### M4 Test q's
#============================== Correct, output 16

# def func1(a):
#     return a ** a

# def func2(a):
#     return func1(a) * func1(a)

# print(func2(2))

#==============================

# def fun(x):
#     global y
#     y = x * x
#     return y

# fun(2)
# print(y)

#==============================

# def fun(x):
#     if x % 2 == 0:
#         return 1
#     else: 
#         return
    
# print(fun(fun(2)) + 1)

#==============================

# dictionary = {'one': 'two', 'three': 'one', 'two': 'three'}
# v = dictionary['one']

# for k in range(len(dictionary)):
#     v = dictionary[v]

# print(v)


#==============================

# def fun(inp=2, out=3):
#     return inp * out

# print(fun(out=2))


#==============================
tup = (1, 2, 4, 8)
tup = tup[-2:-1]
print(tup)
tup = tup[0]
print(tup)

#==============================
# def f(x):
#     if x == 0:
#         return 0
#     return x + f(x - 1)

# print(f(3))


#============================== Correct -> print(k[0])
# What code would you insert instead of the comment to obtain the expecteed output? 
# a
# b
# c

# dictionary = {}
# my_list = ['a', 'b', 'c', 'd']

# for i in range(len(my_list) - 1):
#     dictionary[my_list[i]] = (my_list[i], )

# for i in sorted(dictionary.keys()):
#     k = dictionary[i]
#     # Comment

#==============================
# my_list = ['Mary', 'had', 'a', 'little', 'lamb']

# def my_list(my_list):
#     del my_list[3]
#     my_list[3] = 'ram'

# print(my_list(my_list))


#==============================
# TUPLES - IMMUTABLE SEQUENCE TYPES
# Essentially a read-only list. Cannot be modified during runtime.
# A list with its contents copied over would need to be created if you desire to modify them.

# If you'd like to create a tuple with one element
# You must add a comma at the end
# So as to distinguish it from an ordinary single value
# tup = (1,)
# tup = 1,

# #==============================
# # 'vals()' does not exist. Access dictionary values by using values().


# dd = {
#     "1": "0",
#     "0": "1"
# }

# # for x in dd.values():
# #     print(x, end="")

# #==============================
# foo = (1,2,3)
# foo.index(0)

#==============================
# print(1 // 2)

# in = 1
# print(in)

#==============================

# x = 3
# y = 2
# x = x % y
# print(x)
# x = x % y
# print(x)
# y = y % x

# print(y)

# print(0/1)

# nums = [1,2,3]
# vals = nums
# print(vals)
# print(nums)
# del vals[:]
# print(vals)
# print(nums)

# lst = [i for i in range(-1,-2)]
# print(lst)

#==============================

# lst = [[x for x in range(3)] for y in range(3)]

# print(lst)

# for r in range(3):
#     for c in range(3):
#         if lst[r][c] % 2 != 0:
#             print("#")


#==============================

# i = 0
# while i < i + 2:
#     i += 1
#     print("*")
# else: 
#     print("*")

# =================================

# my_list = [x * x for x in range(5)]

# def fun(lst):
#     print(lst[2])
#     del lst[lst[2]]
#     return lst

# print(fun(my_list))

# # =================================
# # Both arrays will return empty. 

# nums = [1,2,3]
# vals = nums

# del vals[:]

# print(nums)


# # =================================
# # Value 'zero' is not in foo.

# foo = (1,2,3)
# # foo.index(0)

# # =================================
# # Priority - 1 / 2.0 = 0.5.
# # 0.5 ^4.0 is 2.0.

# x = float(2)
# y = float(4)

# print(y ** (1/x))
