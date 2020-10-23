# 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
class Solution:
    def removeDuplicates(self, nums:list)->int:
        fast=1
        slow=0
        count=1
        while fast < len(nums):
            if nums[fast]==nums[slow]:
                count+=1
                if count==2:
                    slow+=1
                    nums[slow]=nums[fast]
                fast+=1
            else:
                slow+=1
                nums[slow]=nums[fast]
                count=1
                fast+=1
        return nums[:slow+1]

a=[1,1,1,2,2,2,3,4,5]
aa=Solution()
print(aa.removeDuplicates(a))



