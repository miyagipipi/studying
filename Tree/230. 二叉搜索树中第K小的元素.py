'''
给定一个二叉搜索树的根节点 root ，和一个整数 k ，
请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）

中序遍历，count变量维护遍历到第几个节点
优化：
1.不用count变量，只要k每次-1即可

进阶：
如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化算法？
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        #中序遍历，count变量维护遍历到第几个节点
        queue = collections.deque()
        #count = 1
        while queue or root:
            while root:
                queue.append(root)
                root = root.left
            root = queue.pop()
            if k == 1:
                return root.val
            k -= 1
            root = root.right