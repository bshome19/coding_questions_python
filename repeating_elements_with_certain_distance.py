# Return True if value of index i and j in a given array are exactly same and if abs(i-j) <= k for a given k
# else return False
""" 
    input: 
        given_list = [1, 2, 3, 1, 1], k = 2
    output: True
    
    input: 
        given_list = [1, 2, 3, 1], k = 2
    output: False
    
    input: 
        given_list = [1, 2, 3, 1, 2, 3, 1] , k = 2  
    output: False
    
    input: 
        given_list = [1, 2, 3, 1, 2, 3, 1] , k = 3  
    output: True

"""


def fun(list1, k):
    dict1 = {}
    flag = False
    for i in range(len(list1)):
        if list1[i] in dict1:
            if abs(dict1[list1[i]] - i) <= k:
                flag = True
            else:
                dict1[list1[i]] = i
        else:
            dict1[list1[i]] = i
            
    if flag:
        return True
    else:
        return False

        
given_list = [1, 2, 3, 1, 2, 3, 1]
k = 2
print(fun(given_list, k))