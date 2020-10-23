# 青蛙跳台阶,一次跳1或2层,跳n层总共有多少种跳法
def aaa(n):
    if n==1 or n==2:
        return n
    return aaa(n-1)+aaa(n-2)


print(aaa(4))


