# 合并两个有序数组  假设nums1有足够的空间
from typing import List
def mergeTwo(nums1:List[int],m:int,nums2:List[int],n:int):
    i=m-1               # nums1最后一位下标
    j=n-1               # nums2最后一位下标
    k=m+n-1             # 输出数组的最后一位下标
    while i >= 0 and j >= 0:
        if nums1[i] < nums2[j]:
            nums1[k] = nums2[j]
            j-=1
            k-=1
        elif nums1[i] >= nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
            k-=1
    while i >= 0:
        nums1[k] = nums1[i]
        i -= 1
        k -= 1
    while j >= 0:
        nums1[k] = nums2[j]
        j-=1
        k-=1
    return  nums1

mergeTwo([1,2,3,4],4,[2,3,4],3)












