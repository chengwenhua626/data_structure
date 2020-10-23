class Node:
    def __init__(self,data):
        self.data=data
        self.left = None
        self.right = None
        self.parent = None
class BST:

    def __init__(self):
        self.root = None
    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False
    def __insert(self,data):
        new_node = Node(data)
        if self.is_empty():
            self.root = new_node
        else:
            parent_node = self.root
            while True:
                if data < parent_node.data:
                    if parent_node.left is None:
                        parent_node.left = new_node
                        break
                    else:
                        parent_node=parent_node.left
                elif data >= parent_node.data:
                    if parent_node.right is None:
                        parent_node.right = new_node
                        break
                    else:
                        parent_node=parent_node.right
    def insert(self,*values):
        for value in values:
            self.__insert(value)
        return self
    # def serch(self,value):
    #     if self.root is None:
    #         raise Exception('空')
    #     else:
    #         node = self.root
    #         while node and value != self.root:
    #
    #     return node

    #层序遍历
    # def cenxu(self,node):














