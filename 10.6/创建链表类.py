class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next= None
    def __repr__(self):
        return "Node({})".format(self.data)

class Linklist:
    def __init__(self):
        self.head=None
    # 列表头部插入结点
    def insert_head(self,data):
        new_node=Node(data)
        if self.head:
            new_node.next=self.head
        self.head=new_node



    # 列表末尾插入结点
    def append(self,data):
        if self.head is None:
            self.insert_head(data)
        else:
            temp=self.head
            while temp.next:
                temp=temp.text
            temp.next=Node(data)


    # 输出
    def __repr__(self):
        current=self.head
        string_str=""
        while current:
            string_str+="{}-->".format(current)
            current=current.next
        return string_str+"END"


    # 指定位置插入结点
    def insert(self,i,data):
        if self.head is None:
            self.insert_head(data)
        elif i==1:
            self.insert_head(data)
        else:
            temp=self.head
            j=1
            pre=temp
            while j<i:
                pre=temp
                temp=temp.next
                j += 1
            node=Node(data)
            pre.text=node
            node.text=temp


    # 插入列表
    def insert_list(self,object:list):
        self.head=Node(object[0])
        temp=self.head
        for i in object[1:]:
            node=Node(i)
            temp.next=node
            temp=temp.next

    # 删除头结点
    def delate_head(self):
        temp=self.head
        if self.head:
            self.head=self.head.next
            temp.next=None
        return temp

    # 删除尾部结点
    def delcte_tail(self):
        temp=self.head
        if self.head.next is None:  #只有头部结点
            self.head=None
        else:
            while temp.next.next:  #当下下个结点不为空
                temp=temp.next
            temp.next=None

     #反转链表
    def reverse(self):
        prev=None
        current=self.head
        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        self.head=prev


    #索引
    def __getitem__(self, index):
        current=self.head
        if current is None:
            raise IndexError('The Link List is empty')
        for _ in range(1,index):
            if current.next is None:
                raise  IndexError('Index out of range')
            current=current.next
        return current
    def get(self,index):
        return self.__getitem__(index)

    #更换值
    def __setitem__(self, index:int,data):
        current=self.head
        if current is None:
            raise IndexError('the link list is empty')
        for i in range (1,index):
            if current.next is None:
                raise IndexError('index out of range')
            current=current.next
        current.data=data
    def set(self,index,data):
        self.__setitem__(index,data)





ll=Linklist()
ll.append(12)
ll.append(12)
ll.insert_head(34)
ll.insert_list([1,2,3])
ll.delate_head()
print(ll)
print(ll.get(1))






