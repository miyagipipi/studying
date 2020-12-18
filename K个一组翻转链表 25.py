#K个一组翻转链表 25
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        #创建一个函数reverse(head, a, b)，能反正[a, b)之间的节点
        def reverseNode(a: ListNode, b: ListNode):
            pre, cur, nex = None, a, a
            while cur != b:
                nex = cur.next
                cur.next = pre
                pre, cur = cur, nex
            return pre
        
        #用两个节点指针a, b使区间 [a, b) 包含 k 个待反转元素
        a = b = head
        for i in range(k):
            if b == None: return head
            b = b.next
        newHead = reverseNode(a, b)
        a.next = self.reverseKGroup(b, k)
        return newHead