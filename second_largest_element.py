# find 2nd largest element in a list

""" 
    input: 
        list = [12, 7, 5, 9, 11]
        
    output: 11

"""


listC = [12, 7, 5, 9, 11]

maxx = 0
sec_max = 0
for i in range(len(listC)):
    if listC[i] > maxx:
        sec_max = maxx
        maxx = listC[i]
        
    elif listC[i] < maxx and sec_max < listC[i]:
        sec_max = listC[i]
            
print(sec_max)