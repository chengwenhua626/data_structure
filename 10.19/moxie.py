class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
class BST:
    def __init__(self):
        self.root = None
    def is_empty(self):
        if self.root is None:
            return True
        return False

    # 增
    def insert(self,value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
        else:
            parent_node = self.root
            while True:
                if value < parent_node.data:
                    if parent_node.left is None:
                        parent_node.left = new_node
                        break
                    else:
                        parent_node = parent_node.left
                else:
                    if parent_node.right is None:
                        parent_node.right = new_node
                        break
                    else:
                        parent_node = parent_node.right
            new_node.parent = parent_node





# 冒泡排序
def bubble(a):
    if len(a)<=1:
        return a
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            a[i],a[j]=a[j],a[i]
    return a

# 选择排序
def select(a):
    if len(a)<=1:
        return a
    for i in range(len(a)-1):
        minlist = i
        for j in range(i+1,len(a)):
            if a[minlist]>a[j]:
                minlist=a[j]
        a[i],a[minlist]=a[minlist],a[i]
    return a











