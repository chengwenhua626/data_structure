class Queue:
    def __init__(self):
        self.entries=[]
        self.size=0
    def __repr__(self):
        return f'{self.entries}'
    def put(self,data):     #入队
        self.entries.append(data)
        self.size+=1
    def pop(self):          #出队
        temp=self.entries[0]
        self.entries=self.entries[1:]
        self.size-=1
        return temp
    def cap(self):   #容量
        return self.size
    def front(self):
        return self.entries[0]
    def get(self,index):
        return self.entries[index]

q=Queue()
q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)
q.put(6)
print(q.get(3))



