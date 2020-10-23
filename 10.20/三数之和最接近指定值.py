# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案
def threeSumClosest(nums, target):
    nums.sort()
    min = abs(nums[0]+nums[1]+nums[2])
    res = nums[0]+nums[1]+nums[2]
    for i in range(len(nums)):
        left = i+1
        right = len(nums)-1
        while left < right:
            sums = nums[i]+nums[left]+nums[right]
            if abs(sums-target)<min:
                min=abs(sums-target)
                res=sums
            if sums>target:
                right-=1
            elif sums<target:
                left-=1
            else:
                return sums
    return res
                


