
# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。

def minSubArrayLen(self, s, nums):
    # 初始长度为无穷大,float('inf')代表无穷大
    left,sums,res=0,0,float('inf')
    for right in range(len(nums)):
        sums+=sums[right]
        while sums>=s:
            if right-left+1<res:
                res=right-left+1
            sums-=nums[left]
            left+=1
    return 0 if res==float('inf') else res








