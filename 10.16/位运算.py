
# 算一个数中1的个数
def hamminWeight(n):
    count = 0
    while n!=0:
        n=n&(n-1)
        count+=1
    return count
print(hamminWeight(9))


#算一组数中只有一个的个数
from typing import List
def singlenumber(nums:List):
    res=0
    for i in nums:
        res=res^i
    return res
