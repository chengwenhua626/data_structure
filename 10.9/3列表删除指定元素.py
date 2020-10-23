class Solution:
    def moveZeros(self,nums,val):
        slow=0
        fast=0
        while fast<len(nums):
            if nums[fast]==val:
                fast+=1
            else:
                nums[slow]=nums[fast]
                fast+=1
                slow+=1

        return  nums[:slow]
aa=Solution()
a=[1,2,0,3,0,4,0,5,0]
print(aa.moveZeros(a,2))
