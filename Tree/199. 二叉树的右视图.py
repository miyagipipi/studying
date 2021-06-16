'''
给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。
BFS算法，每次遍历得到当前层的节点值后，取最后一个元素添加到ans中

补充：
如第23，28行所示，这里每层的元素可以不用一个长度为当前层节点数的queue来维护
因为我们每次肯定是取最右边的节点值，所以可以在每次循环时用当前的节点值覆盖之前的节点值，
这样level_q就可以只存储一个值，可以由一个数组变成一个变量，节约了空间
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        ans = []
        queue =collections.deque()
        queue.append(root)
        while queue:
            level_q = collections.deque()
            #level_q = None
            #size = len(queue)
            for i in range(size := len(queue)):
                node = queue.popleft()
                level_q.append(node.val)
                #level_q = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(level_q.pop())
            #ans.append(level_q)
        return ans