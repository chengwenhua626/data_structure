def count_sort(arr):
    max_value=max(arr)
    count_arr=[0]*(max_value+1)
    for i in range(len(arr)):
        count_arr[arr[i]]+=1
    sort_arr=[]
    for i in range(len(count_arr)):
        for j in range(count_arr[i]):
            sort_arr.append(i)
    return sort_arr


def countSort(nums):
    a=[]
    for i in range(m in(nums),max(nums)+1):
        for j in nums:
            if i==j:
                a.append(i)
    return a


# print(countSort([9,3,5,4,9,1,2,7,8,1,3,6,5,3,4,0,10,9 ,7,9]))
print(count_sort([9,3,5,4,9,1,2,7,8,1,3,6,5,3,4,0,10,9 ,7,9]))


















