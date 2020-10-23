import time
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)


start=time.time()
print(fib(41))
end=time.time()
dur=end-start
print(dur)



# n的阶乘
def jiecheng(n):
    if n==1 or n==2:
        return n
    return n*jiecheng(n-1)