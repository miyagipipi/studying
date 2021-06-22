'''
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交

思路：
如果单链表能按索引查找节点，那会非常简单。但是链表结构是不能随机查找的，
所以可先将链表节点存入List结构中，这样就能按索引来改变节点

第二种方法相比较第一种，节约了List使用的额外空间
要实现3个函数即可：1.找到链表中间节点的函数（用快慢指针解决），2.翻转后半链表（三指针）
                3.合并两链表
'''
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head: return None
        vec = []
        node = head
        while node:
            vec.append(node)
            node = node.next
        
        i, j = 0, len(vec)-1
        while i < j:
            vec[i].next = vec[j]
            i += 1
            if i == j:
                break
            vec[j].next = vec[i]
            j -= 1
        vec[i].next = None

#方法二 原位处理
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return
        
        mid = self.middleNode(head)
        l1 = head
        l2 = mid.next
        mid.next = None
        l2 = self.reverseList(l2)
        self.mergeList(l1, l2)
    
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            nextTemp = curr.next
            curr.next = prev
            prev = curr
            curr = nextTemp
        return prev

    def mergeList(self, l1: ListNode, l2: ListNode):
        while l1 and l2:
            l1_tmp = l1.next
            l2_tmp = l2.next

            l1.next = l2
            l1 = l1_tmp

            l2.next = l1
            l2 = l2_tmp