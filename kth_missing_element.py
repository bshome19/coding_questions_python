# find kth missing element from a given list

""" 
    input: 
        list = [2, 3, 4, 7, 11] , k = 5  
    output: 9
    
    input: 
        list = [1, 2, 3, 4] , k = 2  
    output: 6
    
    input: 
        list = [1, 2, 4] , k = 2  
    output: 5

"""


arr = [2, 3, 4, 7, 11]
k = 5

missing_arr = []
for i in range(1, arr[-1]):
    if i not in arr:
        missing_arr.append(i)
count = len(missing_arr)
    
if count < k:
    val = k - count
    print(arr[-1]+val)
    
else:   
    print(missing_arr[k-1]) 