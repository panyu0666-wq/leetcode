class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
def removeNthFromEnd(self,head:ListNode,n:int)->ListNode:
    # 创建一个虚拟节点
    dummy_head = ListNode(0,head)
    # 创建快慢指针
    slow = fast = dummy_head
    # 快指针比慢指针快n+1步,这样的话快指针到最后末尾的时候，快慢指针恰好差N个，因为要知道待删除的前一个节点，所以差N+1个
    for i in range(n+1):
        fast = fast.next
    # 移动两个指针，直到快速指针达到链表的末尾
    while fast:
        slow = slow.next
        fast = fast.next
    # 通过更新第(n-1)个节点的next指针删除第n个节点
    slow.next = slow.next.next
    
    return dummy_head.next
    