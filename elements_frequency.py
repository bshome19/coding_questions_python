# find frequency of each elements in a list

""" 
    input: 
        list = [0, 31, 31, 5, 31, 42, 42, 0]
        
    output:
        {0: 2, 31: 3, 5: 1, 42: 2}
"""


listA = [0, 31, 31, 5, 31, 42, 42, 0]

res_dict = {}
for ele in listA:
    if ele in res_dict:
        res_dict[ele] += 1
    else:
        res_dict[ele] = 1
        
print(res_dict)