class stack:
    def __init__(self,limit=10):
        self.stack=[]
        self.size=0
    def __str__(self):
        return str(self.stack)
    # 压栈
    def push(self,data):
        self.stack.append(data)
        self.size+=1
    # 弹栈
    def  pop(self):
        temp=self.stack.pop()
        self.size-=1
        return  temp
    # 栈顶
    def peek(self):
        if self.stack:
            return self.stack[-1]
    def sizeee(self):
        return self.size
    def isempty(self):
        return not bool(self.stack)

if __name__ == '__main__':
    stack=stack(10)
    for i in range(10):
        stack.push(i)
    print(stack)
    print(stack.peek())
    for i in range(10):
        stack.pop()
    print(stack)




























