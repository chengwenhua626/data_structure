def mergeSort(nums):
    if len(nums)<=1:
        return nums
    mid = len(nums)//2
    left = nums[0:mid]
    right = nums[mid:]
    return merge(mergeSort(left),mergeSort(right))
def merge(left,right):
    ilist = []
    while left and right:
        if left[0]<right[0]:
            ilist.append(left.pop(0))
        else:
            ilist.append(right.pop(0))
    while right:
        ilist.append(right.pop(0))
    while left:
        ilist.append(left.pop(0))
    return ilist









