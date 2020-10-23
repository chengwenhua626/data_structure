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
                prev=self.get(index-1)
                new_node.next=prev.next
                prev.next=new_node
            self.size+=1
    def remove(self,index):
        if index<0 or index>self.size-1:
            raise Exception('索引越界')
        else:
            if index==0:
                remove_node=self.head
                self.head=remove_node.next
                remove_node.next=None
            elif index==self.size-1:
                prov=self.get(self.size-1)
                remove_node=prov.next
                prov.next=None
                self.tail=prov
            else:
                prev=self.get(index-1)
                remove_node=prev.next
                prev.next=prev.next.next
            self.size-=1
            return remove_node
    def reverse(self):
        curr=self.head
        prev=None
        while curr:
            next_curr=curr.next
            curr.next=prev
            prev=curr
            curr=next_curr
        self.head=prev
    def __repr__(self):
        curr=self.head
        list_str=''
        while curr:
            list_str+=f'{curr}-->'
            curr=curr.next
        return list_str+'END'




a=Linklist()
a.insert(0,3)
a.insert(0,4)
a.insert(0,5)
a.insert(0,6)
a.insert(0,7)
print(a)
a.remove(3)
print(a)
a.reverse()
print(a)