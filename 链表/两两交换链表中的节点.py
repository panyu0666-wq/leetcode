class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
def swapPairs(head:ListNode)->ListNode:
    # 创建虚拟节点
    dummy = ListNode(0)
    dummy.next = head
    current = dummy

    # 只有当后面至少有两个节点时，才需要交换
    while current.next and current.next.next:
        node1 = current.next
        node2 = current.next.next

        # 开始交换步骤
        current.next = node2
        node1.next = node2.next
        node2.next = node1
        
        # 将current移动到下一节点对的前驱节点
    return dummy.head