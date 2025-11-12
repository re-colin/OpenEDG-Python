lst = [7, 2, 3, 4]

# Insert number (item) 6 at index 1
lst.insert(1, 6)

# 6 will be slotted into index 1, where each item after it will be pushed to the right
print(lst) # [1, 6, 2, 3, 4]

for i in range(len(lst)):
    lst.insert(i, 1)

print(lst)

# Slicing / Copying lists

# [:] is syntax for slicing - extracting a portion of a list and copying it into another list.
nums = [4, 8, 15, 16]
sec = nums[:]

# Modifying the copy - nums array will stay intact
del sec[2] 
print("nums:", nums)
print("sec:", sec)

nums = [2, 3, 7, 6]
sec = nums 

# Modifying both arrays - nums and sec refer to the same object in memory
del sec[2] 

print("nums:", nums)
print("sec:", sec)