# find k nearest values of given number from a given list

""" 
    input: 
        k = 5
        given number =  50
        list = [1, 3, 5, 1, 42, 40, 0, 44, 41, 2, 4, 50, 59, 7, 47, 60, 2, 53, 100, 99, 70]
        
    output:
        [50, 53, 47,  44, 42]
"""


def fun(given_list, given_num, k):
    dict1 = {}
    for ele in given_list:
        diff = given_num - ele if given_num > ele else ele - given_num
        dict1[ele] = diff
    dict1 = dict(sorted(dict1.items(), key=lambda x: x[1]))
    
    res = []
    count = 0
    for key in dict1:
        if count >= k:
            break
        else:
            res.append(key)
            count += 1
            
    return res
        

A = [1, 3, 5, 1, 42, 40, 0, 44, 41, 2, 4, 50, 59, 7, 47, 60, 2, 53, 100, 99, 70]
num = 50

print(fun(given_list=A, given_num=num , k=5))