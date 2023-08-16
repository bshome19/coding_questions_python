# Two sum problem: return the index of two elements whose sum is equal to the target 
#                   else return False if no such element is there in the list

""" 
    input: 
        list = [1, 7, 2, 5, 9, 17]
        target = 11
        
    output: (4, 2) or (2, 4)

"""


def two_sum(listG, target):
    dictG = {}
    for i in range(len(listG)):
        diff = target - listG[i]
        if listG[i] in dictG:
            return i, dictG[listG[i]]
        else:
            dictG[diff] = i
            
    return False
        

listA = [1, 7, 2, 5, 9, 17]
t_num = 11

print(two_sum(listA, t_num))