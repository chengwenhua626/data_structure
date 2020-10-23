# init的作用
#     让一个呈结构化分布的代码文件(以文件夹形式组织)变成可以被导入import的软件包


# 最大公约数
def max_common_divisor1(a,b):
    if a-b == 0:
        return a
    max1 = max(a,b)
    min1 = min(a,b)
    if max1%min1 == 0:
        return min1
    return max_common_divisor1(min1,max1%min1)
# print(max_common_divisor1(12,8))






# (75)给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色
# def sortColors(nums):
#     numsa=[]
#     numsb=[]
#     numsc=[]
#     for i in nums:
#         if i==0:
#             numsa.append(i)
#         if i==1:
#             numsb.append(i)
#         if i==2:
#             numsc.append(i)
#     return numsa+numsb+numsc
#
# a=[1,2,0,0,2,2,0,1,1,0,2]
# print(sortColors(a))
# # 荷兰\冒泡排序
# def sortColors(nums):
#     for i in range(len(nums)-1):
#         if len(nums) <= 1:
#             return nums
#         for j in range(len(nums)-i-1):
#             if nums[j]>nums[j+1]:
#                 nums[j],nums[j+1]=nums[j+1],nums[j]
#     return nums
# # a=[1,2,0,0,2,2,0,1,1,0,2]
# # print(sortColors(a))
def sortColors(nums):
    a=c=0
    b=len(nums)-1
    while c<=b:
        if c==0:
            nums[a],nums[c] = nums[c],nums[a]
            a+=1
            c+=1
        elif c==2:
            nums[c],nums[b] = nums[b],nums[c]
            b-=1
        else:
            c+=1
    return nums



















# (5)
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
def longestPalindrome(strs:str):
    length = len(strs)
    if length<2:
        return strs
    maxlen = 1
    res = strs[0]
    for i in range(length-1):
        odd = centerSpread(strs,i,i)
        even = centerSpread(strs,i,i+1)
        maxstr = odd if len(odd) > len(even) else even
        if len(maxstr) >maxlen:
            maxlen = len(maxstr)
            res = maxstr
    return res


def centerSpread(strs,left,right):
    length = len(strs)
    i = left
    j = right
    while i>=0 and j< length:
        if strs[i]==strs[j]:
            i-=1
            j+=1
        else:
            break
    return strs[i+1:j]







