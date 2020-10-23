class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.size = 0
# def reverse(head):
#     cur = head
#     pre = cur.next






# # 两两交换链表中的结点
# def twotwochange(head):
#     new_node = Node(0)
#     cur = head
#     while cur:
#         pre = cur.next
#         new_node.net=pre
#         pre.next = cur
#         cur=cur.next.next
#     return new_node.next











# 数组反转
def reverse(nums):
    a = nums[-1:-len(nums) - 1:-1]
    return a

# print(reverse([1, 2, 3, 4, 5, 6, 7]))
