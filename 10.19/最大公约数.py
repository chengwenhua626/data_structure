def max_common_divisor(a,b):
    max1 = max(a,b)
    min1 = min(a,b)
    if max1%min1 == 0:
        return min1
    for i in range(min1//2,0,-1):
        if max1%i==0 and min1%i==0:
            return i
print(max_common_divisor(20,8))

# 辗转相除法,l两个数都比较大的时候取余比较麻烦
# 两个正整数(a>b)的最大公约数,
def max_common_divisor1(a,b):
    max1 = max(a,b)
    min1 = min(a,b)
    if max1%min1 == 0:
        return min1
    return max_common_divisor1(min1,max1%min1)
print(max_common_divisor(12,8))

# 更相减损术
# 两个正整数a,b(a>b) 最大公约数等于a-b的差和b之间的最大公约数
def max_common_divisor2(a,b):
    if a-b == 0:
        return a
    max1 = max(a,b)
    min1 = min(a,b)

    return max_common_divisor1(max1-min1,min1)
print(max_common_divisor(12,5))






