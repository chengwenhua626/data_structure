def twosums(nums,target):
    nums.sort()
    print(nums)
    aaa = []
    for a in range(len(nums)-2):
        if nums[a]==nums[a-1] and a>0:
            continue
        left = a+1
        right = len(nums)-1
        while left < right:
            he=nums[a]+nums[left]+nums[right]
            if he < target:
                left += 1
            elif he > target:
                right -= 1
            else:
                aaa.append([nums[a],nums[left],nums[right]])
                while left<right and nums[left]==nums[left+1]:
                    left+=1
                while left<right and nums[right]==nums[right-1]:
                    right-=1
                left+=1
                right-=1
    return aaa



a=[1,-1,4,0,3]
print(twosums(a,0))




















