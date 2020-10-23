def swap(array,a,b):
    array[a],array[b]=array[b],array[a]
def quickSort(ilist,start,end):
    if start>=end:
        return
    mid = partition(ilist,start,end)
    quickSort(ilist,start,mid-1)
    quickSort(ilist,mid+1,end)


def partition(ilist,start,end):
    pivot=ilist[start]
    p=start+1
    q=end
    while p<=q:
        while p<=q and ilist[p]<pivot:
            p+=1
        while p<=q and ilist[q]>=pivot:
            q-=1
        if p<q:
            swap(ilist,p,q)
    swap(ilist,start,q)
    return q


# 单指针遍历法
def partition1(arr,start,end):
    pivot = str(start)
    mark = start
    for i in range(start+1,end+1):
        if arr[i]<pivot:
            mark+=1
            arr[mark],arr[i]=arr[i],arr[mark]
    arr[start]=arr[mark]
    arr[mark]=pivot
    return mark



a=[0,3,2,8,5,6]
print(a)
quickSort(a,0,5)
print(a)




