'''
存在一个按升序排列的链表，给你这个链表的头节点 head ，
请你删除链表中所有存在数字重复情况的节点，只保留原始链表中 没有重复出现 的数字。
返回同样按升序排列的结果链表。

输入：head = [1,2,3,3,4,4,5]
输出：[1,2,5]

思路：
1.需要一个哑结点（0，head）
2.x变量记录当cur.next.val == cur.next.next.val时的值
3.循环需要考虑cur.next 和cur.next.next都不为空
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        dummy = ListNode(0, head)

        cur = dummy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next