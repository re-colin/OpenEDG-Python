str1 = "Where are the snows of yesteryear?"

str1_list = str1.split()
print(str1_list)

ord_list = []

for s in range(len(str1_list)):
    ordc = 0
    for c in str1_list[s]:
        ordc += ord(c)
        # print(str1_list[s])

    ord_list.append(ordc)

print(ord_list)
print(str1_list)
ord_list.sort()
str1_list.sort()

print(ord_list)
print(str1_list)