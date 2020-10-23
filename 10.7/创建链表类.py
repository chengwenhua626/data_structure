class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return "Node({})".format(self.data)

class Linklist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def get(self,index):
        curr=self.head
        for _ in range(index):
            curr=curr.next
        return curr
    # 增..........................................................
    def insert(self,index,data):
        new_node=Node(data)
        if index<0 or index>self.size:
            raise Exception('索引越界')
        else:
            if self.size==0:
                self.head=new_node
                self.tail=new_node
            # 头部增加
            elif index==0:
                new_node.next=self.head
                self.head=new_node
            # 尾部插
            elif index==self.size:
                self.tail.next=new_node
                self.tail=new_node
            # 中间插
            else:
                prew=self.get(index-1)
                new_node.next=prew.next
                prew.next=new_node
            self.size+=1

    # 删..........................................................
    def remove(self,index):
        if index<0 or index>=self.size:
            raise Exception('索引越界')
        if index==0:
            remove_node=self.head
            self.head=remove_node.next
            remove_node.next=None
        elif index==self.size-1:
            prew=self.get(index-1)
            remove_node=prew.next
            self.tail = prew
            prew.next=None
        else:
            prew=self.get(index-1)
            remove_node=prew.next
            prew.next=prew.next.next
        self.size-=1
        return remove_node

    # 翻转.....................................................
    def reverse(self):
        prev=None
        current=self.head
        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        self.head=prev

    # 输出......................................................
    def __repr__(self):
        curr=self.head
        list_str = ''
        while curr:
            list_str += '{}-->'.format(curr)
            curr = curr.next
        return list_str+'END'



a=Linklist()
a.insert(0,3)
print(a)
a.insert(1,4)
print(a)
















