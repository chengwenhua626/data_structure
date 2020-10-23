class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Tree:
    def __init__(self):
        self.root=None
    def add(self,item):
        node=Node(item)
        if self.root is None:
            self.root=node
        else:
            temp=[self.root]
            while True:
                pop_temp=temp.pop(0)
                if pop_temp.left==None:
                    pop_temp.left=node
                    return
                elif pop_temp.right==None:
                    pop_temp.right=node
                    return
                else:
                    temp.append(pop_temp.left)
                    temp.append(pop_temp.right)
    def __repr__(self):
        curr=self.root







t=Tree()
t.add(5)
t.add(6)
print(t)