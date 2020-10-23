class solitional:

    def removeDuplicated(self,nums:list)->int:
        slow=0
        fast=1
        while fast<len(nums):
            if nums[fast]==nums[slow]:
                fast+=1
            else:
                slow+=1
                nums[slow]=nums[fast]
                fast+=1
        return slow+1



s=solitional()
print(s.removeDuplicated([1,2,2,3,4,5]))




















