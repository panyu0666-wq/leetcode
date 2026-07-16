class ListNode:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next
def getIntersectionNode(self,headA:ListNode,headB:ListNode)->ListNode:
    lenA,lenB = 0,0
    cur = headA
    while cur:
        cur = cur.next
        lenA+=1
    cur = headB
    while cur:
        cur = cur.next
        lenB+=1
    curA,curB = headA,headB
    if lenA>lenB:    # 让curB为最长链表的头,lenB为其长度
        curA,curB = curB,curA
        lenA,lenB = lenB,lenA
    for _ in range(lenB-lenA):
        curB = curB.next
    while curA:
        if curA==curB:
            return curA
        else:
            curA = curA.next
            curB = curB.next
    return None