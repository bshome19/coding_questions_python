list1 = [12, 7, 5, 9, 11]

max1 = 0
sec_max = 0
for i in range(len(list1)):
    if list1[i] > max1:
        sec_max = max1
        max1 = list1[i]
        
    elif list1[i] < max1 and sec_max < list1[i]:
        sec_max = list1[i]
            
print(sec_max)