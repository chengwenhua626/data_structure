# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 示例:
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]

class Solution:
    def moveZeros(self,nums):
        slow=0
        fast=0
        while fast<len(nums):
            if nums[fast]==0:
                fast+=1
            else:
                nums[slow]=nums[fast]
                fast+=1
                slow+=1
        for i in range(slow,len(nums)):
            nums[i]=0
        return  nums
aa=Solution()
a=[1,2,0,3,0,4,0,5,0]
print(aa.moveZeros(a))






