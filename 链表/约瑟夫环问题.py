class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def josephus_linked_list(n,k):
    if n<=0 or k<=0:
        return None
    # 构建包含n个节点的单向循环链表
    head = Node(1)
    curr = head
    for i in range(2,n+1):
        curr.next = Node(i)
        curr = curr.next
    # 循环结束，curr指向最后一个节点，将其与head相连形成循环
    curr.next = head
    # 初始化prev和curr
    # 为了方便删除，我们将prev定位在最后一个节点,curr定位在第一个节点
    prev = curr
    curr = head
    # 开始模拟
    # 当curr的下一个节点还是自己时，说明圈内还剩下最后一人
    while curr.next != curr:
        for _ in range(k-1):
            prev = curr
            curr = curr.next

        # 此时删除curr
        prev.next = curr.next
        curr = prev.next
    return curr.data
n = 5
k = 2
survivor = josephus_linked_list(n,k)
print(survivor)
