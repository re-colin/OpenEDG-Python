# # ================= RANGE FUNCTION

# for i in range(-1, 1):
#     print(i)

# for i in range(-1, 5):
#     print(i)

# # ================= LIST COPYING

# nums = [1, 2]
# vals = nums

# vals.append(3)
# print(nums)
# print(vals)

# # ================= LIST COPYING

# nums = [1, 2]
# vals = nums[:]   

# vals.append(3)

# print(nums)  ## [1, 2]
# print(vals)  ## [1, 2, 3]

# # ================= LIST SLICING

# nums = [1, 2, 3]  # Equivalent to x[slice(None, None, None)]
# vals = nums

# del vals[1:2]

# print(vals)
# print(nums)

# # ================= Range & nested arrays/2d matrices

# t = [ [  3 - i for i in range(3) ] for j in range(3) ] ## Make an array from 3 to 1 three times
# # --->
# # [[3, 2, 1],
# # [3, 2, 1],
# # [3, 2, 1]]

# s = 0

# for i in range(3):
#     # print(i)
#     print(t[i])
#     s += t[i][i]

# print(s)

# # ================= BITWISE LOGIC

# a = 1
# b = 0
# c = a & b  # AND
# d = a | b  # OR 
# e = a ^ b  # Bitwise XOR

# print(f"c: {c}")
# print(f"d: {d}")
# print(f"e: {e}")

# print(c + d + e)  # --> 2

# # ================== Q: Correct
# Runtime error: Out of range list index.
# Actual data is
# [[0, 1, 2, 3], 
# [0, 1, 2, 3]] 
# my_list = [[0, 1, 2, 3] for i in range(2)]
# print(my_list[1][0])
# print(my_list)

# # ================== Q  
# my_list_1 = [1, 2, 3]
# my_list_2 = []

# for v in my_list_1:
#     my_list_2.insert(0, v)

# print(my_list_2)

# # ================== Q
# my_list = [3, 1, -2]
# print(my_list[my_list[-1]])

# # ================== Q
# var = 0
# while var < 6:  
#     var += 1   
#     if var % 2 == 0:
#         continue
#     print("#") # 3

# # ================== Q
# var = 0
# while var < 6:
#     var += 1
#     if var % 2 == 0:
#         continue
#     print("#")

# # ================== Q
# i = 0
# while i <= 3:
#     i += 2
#     print("#")


# # ================== LIST SLICING
# my_list = [1, 2, 3, 4]

# Split from -3 index to before -1 index
# print(my_list[-3:-1])    #--->  [ 2, 3 ]

# # ================== Q

# This loop will print only one star before termination.
# i = 0

# while i <= 5:
#     i += 1
#     if i % 2 == 0:
#         break
#     print("*")

# # ================== BITWISE LEFT SHIFTING
# This is a binary operator.
# 0b1010  = 10.

# Here, each bit of var is shifted by n places to the left.
# 1:  var = 2  
# 2:  var = 4
# 3:  var = 8
# 4:  var = 16   More than 10, loop exits
# var = 1
# while var < 10:
#     print("#", var)
#     var = var << 1  # adding to itself


