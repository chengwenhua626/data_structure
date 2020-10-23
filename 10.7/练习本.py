class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return f'Node({self.data})'
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
    # 添加
    def insert(self,index,data):
        new_node=Node(data)
        if index<0 or index>self.size:
            raise Exception('索引越界')
        else:
            if self.size==0:
                self.head=new_node
                self.tail=new_node
            elif index==0:
                new_node.next=self.head
                self.head=new_node
            elif index==self.size:
                self.tail.next=new_node
                self.tail=new_node
            else:
                prew=self.get(index-1)
                new_node.next=prew.next
                prew.next=new_node
        self.size+=1
    # 删除
    def remove(self,index):
        if index<0 or index>self.size:
            raise Exception('索引越界')
        else:
            if index==1:
                remove_node=self.head
                self.head=remove_node.next
                remove_node.next=None
            elif index==self.size-1:
                prew=self.get(index-1)
                remove_node=prew.next
                self.tail=prew
                prew.next=None
            else:
                prew=self.get(index-1)
                remove_node=prew.next
                prew.next=prew.next.next
            self.size-=1
        return remove_node
    # 翻转
    def reverse(self):
        prew=None
        current=self.head
        while current:
            next_current=current.next
            current.next=prew
            prew=current
            current=next_current
        self.head=prew

    def __repr__(self):
        curr=self.head
        list_str=''
        while curr:
            list_str+=f'{curr}-->'
            curr=curr.next
        return  list_str+'end'

a=Linklist()
a.insert(0,4)
a.insert(1,3)

print(a)
a.insert(1,2)
print(a)
a.reverse()
print(a)











