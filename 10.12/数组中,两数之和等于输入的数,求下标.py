def twosums(nums,target):
   nums.sort()
   print(nums)
   begin=0
   end=len(nums)-1
   while begin < end:
      curr=nums[begin]+nums[end]
      if curr==target:
         print(begin,end)
         begin+=1
         end-=1
      else:
         if curr<target:
            begin+=1
         else:
            end-=1
a=[1,5,4,2,3]
twosums(a,7)



def two_index(nums:list,target:int):
    for i in range(len(nums)):
        index1=target-nums[i]
        if index1 in nums and i!=nums.index(index1):
            return i,nums.index(index1)



# a=[1,2,2,4,5]
# print(two_index(a,4))
#
class Solution:
   def twoSum(self,nums,target):
      d = {}
      n = len(nums)
      for x in range(n):
         if target - nums[x] in d:
            return d[target-nums[x]],x
         else:
            d[nums[x]] = x








