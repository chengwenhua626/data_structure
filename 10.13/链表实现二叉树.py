from pprint import pformat
class Node:
    def __init__(self,data):
        self.data=data
        self.parrent=None
        self.left=None
        self.right=None
    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.data)
        return pformat({'%s'%(self.data):(self.left,self.right)},indent=4)
# 二叉搜索树
class BinaryhSearhTree:
    def __init__(self):
        self.root=None

    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False
    #插入
    def __insert(self,value):
        new_node = Node(value)
        if self.is_empty():
            self.root=new_node
        else:
            parrent_node=self.root
            while True:
                if value < parrent_node.data:
                    if parrent_node.left is None:
                        parrent_node.left = new_node
                        break
                    else:
                        parrent_node = parrent_node.left
                elif value >= parrent_node.data:
                    if parrent_node.right is None:
                        parrent_node.right = new_node
                        break
                    else:
                        parrent_node = parrent_node.right
            new_node.parrent=parrent_node
    #插入
    def insert(self,*values):
        for value in values:
            self.__insert(value)
        return self
    def __repr__(self):
        return str(self.root)

    #查找(返回值对应的结点,)
    def serch(self,value):
        if self.is_empty():
           raise Exception('========')
        else:
            node=self.root
            while node and value!=node.data:
                if value < node.data:
                    node=node.left
                else:
                    node=node.right
            # print(node)
        return node
    def is_right(self,node):    #判断当前节点是否是父结点的孩子
        return node==node.parrent.right

    #删除结点的内置函数
    def __reassign_nodes(self,node,new_children):
        if new_children is not None:
            new_children.parrent = node.parrent
        if node.parrent is not None:
            if self.is_right(node):
                node.parrent.right = new_children
            else:
                node.parrent.left = new_children
        else:
            self.root = new_children
    #删除结点
    def remove(self,data):
        node = self.serch(data)
        if node is not None:
            if node.left is None and node.right is None:
                self.__reassign_nodes(node,None)
            elif node.left is None:
                self.__reassign_nodes(node,node.right)
            elif node.right is None:
                self.__reassign_nodes(node,node.left)
            else:
                tmp_node = self.get_max(node.left)
                self.remove(tmp_node.data)
                node.data = tmp_node.data
    #获得最大值
    def get_max(self,node=None):
        if node is None:
            node = self.root
        if not self.is_empty():
            while node.right is not None:
                node = node.right
        return node
    def get_min(self,node=None):
        if node is None:
            node = self.root
        if not self.is_empty():
            node=self.root
            while node.left is not None:
                node = node.left
        return node


    #前序遍历复杂方法
    def perOrder1(self,node):
        if not node:
            return None
        print(node.data)
        self.perOrder(node.left)
        self.perOrder(node.right)
    #前序遍历数(简单方法)
    def perOrder(self,node):
        stack = [node]
        while len(stack)>0:
            print(node.data,end=' ')
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            node = stack.pop()
    #中序遍历
    def in_order_stack(self,node):
        stack=[]
        while node or len(stack)>0:
            while node:
                stack.append(node)
                node=node.left
            if len(stack)>0:
                node=stack.pop()
                print(node.data,end=' ')
                node=node.right
    #后序遍历
    def post_order(self,node):
        if node is None:
            return False
        stack1=[]
        stack2=[]
        stack1.append(node)
        while stack1:
            node = stack1.pop()
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
            stack2.append(node)
        while stack2:
            print(stack2.pop().data,end=' ')

    #层序遍历
    def level_order(self,root):
        from queue import Queue
        queue = Queue()
        queue.put(root)
        while not queue.empty():
            node = queue.get()
            print(node.data)
            if node.left:
                queue.put(node.left)
            if node.right:
                queue.put(node.right)



b=BinaryhSearhTree()
print(b.insert(4,2,1,3,5,4,6))
# print(b.remove(1))
# print(b.perOrder(b.root))
# print(b.serch(2))
b.perOrder(b.root)
print()
b.in_order_stack(b.root)

















