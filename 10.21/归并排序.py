
def mergeSort(ilist):
    if len(ilist)<=1:
        return ilist
    middle = len(ilist)//2
    left,right = ilist[0:middle],ilist[middle:]
    return merge(mergeSort(left),mergeSort(right))


def merge(left,right):
    mlist=[]
    while left and right:
        if left[0]>=right[0]:
            mlist.append(right.pop(0))
        else:
            mlist.append(left.pop(0))
    while left:
        mlist.append(left.pop(0))
    while right:
        mlist.append(right.pop(0))
    return mlist











