class Heap:
    def __init__(self):
        self.data_list = []

    #返回父节点的下标
    def get_parent_index(self,index):
        if index<0 or index >= len(self.data_list)-1:
            return None
        else:
            return (index-1)>>1
    #交换数组的两个元素
    def swap(self,a,b):
        self.data_list[a],self.data_list[b] = self.data_list[b],self.data_list[a]

    #添加元素
    def insert(self,data):
        self.data_list.append(data)
        index = len(self.data_list)-1
        parent = self.get_parent_index(index)
        while parent is not None and self.data_list[parent]<self.data_list[index]:
            self.swap(index,parent)
            index = parent
            parent = self.get_parent_index(parent)
    # 删除堆顶元素
    def pop(self):
        remove_data = self.data_list[0]
        self.data_list[0] = self.data_list[-1]
        # 删除最后一个元素
        del self.data_list[-1]
        # 从顶端堆化
        self.heapify(0)
        return remove_data
    # 堆化
    def heapify(self,index):
        total_index = len(self.data_list)-1
        while True:
            maxvalue_index = index
            if 2*index+1<total_index and self.data_list[2*index+1]>self.data_list[maxvalue_index]:
                maxvalue_index = 2 * index + 1
            if 2*index+2<total_index and self.data_list[2*index+2]>self.data_list[maxvalue_index]:
                maxvalue_index = 2 * index + 2
            if maxvalue_index == index:
                break
            self.swap(index,maxvalue_index)
            index = maxvalue_index





if __name__ == '__main__':
    heap=Heap()
    heap.insert(1)
    heap.insert(2)
    heap.insert(3)
    print(heap.data_list)






