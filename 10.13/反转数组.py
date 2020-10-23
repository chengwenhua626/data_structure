# 反转数组
def reverse(list1):
    list2=[]
    for i in range(-1,-len(list1)-1,-1):
        list2.append(list1[i])
    return list2

a=[1,2,3,4,5]
print(reverse(a))