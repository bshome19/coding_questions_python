def fun(list1, given_num, k):
    dict1 = {}
    for ele in list1:
        diff = given_num - ele if given_num > ele else ele - given_num
        dict1[ele] = diff

A = [1, 3, 5,1, 42, 40, 0, 44, 41, 2, 4, 50, 59, 7, 47, 60, 2, 53, 100, 99, 70]
given_num = 50
#find 5 nearest values of 50 from the list
fun(A, given_num , k = 5)
#result:
#50, 53, 47,  44, 42