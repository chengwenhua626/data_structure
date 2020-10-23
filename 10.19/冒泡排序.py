from rand_list import randomList
# 冒泡排序
def bubble(a):
    if len(a)<=1:
        return a
    for i in range(len(a)-1):
        Flag=True
        for j in range(len(a)-i-1):
            print(a,i)
            if a[j]>a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                Flag=False
        if Flag:
            break
    return a

# 选择排序 最小值每次都放在最前面
# 内层循环负责找每一轮循环的最小值,
def select(a):
    if len(a)<=1:
        return a
    for i in range(len(a)-1):
        minlist=i
        for j in range(i+1,len(a)):
            if a[minlist]>a[j]:
                minlist=j
        a[i],a[minlist]=a[minlist],a[i]
        print('第%s次'%(i),a)
    return a

llist=randomList.randonList(5)
print(select(llist))


# 插入排序(像扑克牌)
#  遍历除第一张之后的每一张,右边是还没有插入的牌,左边是已经排好序的
def insertSort(nums):
    if len(nums) <= 1:
        return nums
    for right in range(1,len(nums)):
        target = nums[right]
        for left in range(0,right):
            if nums[left] > target:
                nums[left+1:right+1] = nums[left:right]
                nums[left] = target
    return nums


# 插入排序(链表)
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.head = None
def insertSortlist(head):
    dummy = Node(0)
    pre = dummy
    cur = head
    while cur is not None:
        temp = cur.next
        while pre.next and pre.next.data<cur.data:
            pre=pre.next
        cur.next = pre.next
        pre.next = cur
        cur=temp
        pre = dummy
    return dummy.next







