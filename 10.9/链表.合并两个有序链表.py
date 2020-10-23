class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return f'{self.data}'
def add_two_list(a1,a2):
    node=Node(0)
    curr=node
    while a1 and a2:
        if a1.data<a2.data:
            curr.next=a1
            a1=a1.next
        else:
            curr.next = a2
            a2=a2.next
        curr=curr.next
    if a1 is None:
        curr.next=a2
    if a2 is None:
        curr.next=a1
    head=node.next
    curr=head
    strr=''
    
    while curr:
        strr+=f'{curr}--'
        curr=curr.next
    return strr
if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(7)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = None
    node5.next = node6
    node6.next = node7
    node7.next = node8
    node8.next = None
    print(add_two_list(node1,node5))














