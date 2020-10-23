def binarySearch(nums,val):
    left = 0
    right = len(nums)-1
    while left <= right:
        if val == left:
            return left
        elif val == right:
            return right
        else:
            mid = (left+right)//2
            if val < nums[mid]:
                right=mid
            elif val > nums[mid]:
                left = mid
            else:
                return mid








