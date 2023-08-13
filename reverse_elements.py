# reverse the elements in a given list without using a new list

""" 
    input: 
        list = [31, 2, 9, 3, 15, 7]
        
    output:
        [7, 15, 3, 9, 2, 31]
"""


listB = [31, 2, 9, 3, 15, 7]
n = len(listB)
for i in range(n//2):
    listB[i], listB[len(listB)-1-i] = listB[len(listB)-1-i], listB[i]

print(listB)