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

#自己写的
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        #if not head: return None
        pre = None
        now = nex = head
        for i in range(k):
            if now == None: return head
            now = now.next
            
            
        now = head
        for i in range(k):
            nex = now.next
            now.next = pre
            pre = now
            now = nex
        
        head.next = self.reverseKGroup(now, k)
        return pre
'''没有特意去写一个reverse函数，而是先将now作为侦查兵，
去看有没有k个节点能满足要求（L33-L35)
这里我之前写的是range(k-1)，因为34行和35行的顺序是倒着的，
导致无法解决一些问题（节点数正好是k的整数倍），所以加了第30行才解决。
但实际上把34和35行换一下位置，就可以range(k)了。