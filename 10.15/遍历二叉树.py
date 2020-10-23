# 前序遍历复杂方法
def perOrder1(self, node):
    if not node:
        return None
    print(node.data)
    self.perOrder(node.left)
    self.perOrder(node.right)


# 前序遍历数(简单方法)
def perOrder(self, node):
    stack = [node]
    while len(stack) > 0:
        print(node.data, end=' ')
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        node = stack.pop()


# 中序遍历
def in_order_stack(self, node):
    stack = []
    while node or len(stack) > 0:
        while node:
            stack.append(node)
            node = node.left
        if len(stack) > 0:
            node = stack.pop()
            print(node.data, end=' ')
            node = node.right