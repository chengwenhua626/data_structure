"""
Author: cheng
Create: 2020/10/10 11:12
"""

# 删除链表特定值203
class Node:
    def __init__(self,data):
        self.data=data
        self.size=0
    # def __repr__(self):
    #     return f'{self.data}'

def removeElement(tou,val):
    node=Node(0)
    curr = node
    node.next=tou
    while curr.next:
        if curr.next.data==val:
            temp=curr.next
            curr.next=curr.next.next
            temp.next=None
        else:
            curr=curr.next
            print(curr.data,'++++++')
    return node.next
def printlist(tou):
    curr=tou
    strr=''
    while curr:
        strr+=f'{curr.data}-->'
        curr=curr.next
    return strr



if __name__ == '__main__':
    node1=Node(1)
    node2=Node(2)
    node3=Node(3)
    node4=Node(4)
    node5=Node(5)
    node1.next=node2
    node2.next=node3
    node3.next=node4
    node4.next=node5
    node5.next=None
    print(printlist(removeElement(node1,3)))















# 链表有序链表合并两个