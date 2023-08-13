list3 = [1, 2, 9, 3, 5]
n = len(list3)
for i in range(n//2):
    list3[i], list3[len(list3)-1-i] = list3[len(list3)-1-i], list3[i]

print(list3)