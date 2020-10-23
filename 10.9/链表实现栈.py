class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def __repr__(self):
        return f'{self.data}'

class Linkstack:
    def __init__(self):
        self.top=None
        self.size=0
    def push(self,item):
        node=Node(item)
        if self.top:
            node.next=self.top
            self.top=node
        else:
            self.top=node
        self.size+=1
    def pop(self):
        if self.pop==None:
            raise IndexError('pop from empty stack')
        else:
            node=self.top
            self.top=node.next
            node.next=None
            self.size-=1
            return node
    def isempty(self):
        return self.top is None

    def sizee(self):
        return self.size
    def __str__(self):
        current=self.top
        string=''
        while current:
            string+=f'{current}-->'
            current=current.next
        return string




if __name__ == '__main__':
    a=Linkstack()
    for i in range(10):
        a.push(i)
    print(a)
    a.pop()
    print(a)
    print(a.isempty())
    print(a.sizee())




















