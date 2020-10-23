# 24  两两交换链表结点
class Node:
    def __init__(self,data):
        self.data=data
        self.size=0
    # def __repr__(self):
    #     return f'{self.data}'


def twotwochange(head):
    node=Node(0)
    node.next=head
    curr=node
    while curr.next and curr.next.next:
        slow=curr.next
        fast=curr.next.next
        curr.next=fast
        slow.next=fast.next
        fast.next=slow
        curr=curr.next.next
        # printlist(curr.data)
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
    print(printlist(twotwochange(node1)))


