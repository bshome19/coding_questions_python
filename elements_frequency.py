
list2 = [2, 5, 3, 2, 2, 6, 7]

dict1 = {}
for ele in list2:
    if ele in dict1:
        dict1[ele] += 1
    else:
        dict1[ele] = 1
        
print(dict1)