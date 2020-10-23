class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return self.data
class Queue:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def put(self,item):
        node=Node(item)
        if self.head is None:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node
        self.size+=1
    def pop(self):
        if self.head is None:
            raise IndexError('队列为空')
        else:
            curr=self.head
            self.head=curr.next
            curr.next=None
        self.size-=1
        return curr
    def __repr__(self):
        curr=self.head
        strr=''
        while curr:
            strr+=f'{curr.data}-->'
            curr=curr.next
        return strr

if __name__ == '__main__':

    q=Queue()
    q.put(23)
    q.put(45)
    q.put(47)
    q.put(49)
    print(q)
    q.pop()
    print(q)


