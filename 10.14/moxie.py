# def twosums1(nums:list,tager):
#     for i in range(len(nums)):
#         if tager-nums[i] in nums and i!=nums.index(tager-nums[i]):
#             print(i,nums.index(tager-nums[i]))
# a=[1,2,3,4,5]
# print(twosums1(a,4))


def twosums2(nums:list,tager):
    dic={}
    n=len(nums)
    for i in range(n):
        if tager-nums[i] in dic:
            print( i,dic[tager-nums[i]])
        else:
            dic[nums[i]]=i

a=[1,2,3,4,5]
twosums2(a,4)



