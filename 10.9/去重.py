class solitional:
    # 去重
    def quchong(self,a:list)->int:
        slow=0
        fast=0
        while fast<len(a):
            if a[slow]==a[fast]:
                fast+=1
            else:
                slow+=1
                a[slow]=a[fast]
                fast+=1
        return a[:slow+1]
    # 移动零
    def yidongling(self,a:list):
        slow=0
        fast=0
        while fast<len(a):
            if a[fast]!=0:
                a[slow] = a[fast]
                slow+=1
                fast+=1
            else:
                fast+=1
        for i in range(slow+1,len(a)):
            a[i]=0
        return a



    def __repr__(self):
        return a
if __name__ == '__main__':
    q=solitional()
    b=q.quchong([1,1,1,1,1,2,3,3,4,4,5,6])
    print(b)

    print(q.yidongling([1,0,1,1,1,0,1,2,3,3,4,4,5,6]))









