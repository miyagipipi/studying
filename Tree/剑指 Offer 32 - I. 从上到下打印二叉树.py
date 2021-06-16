'''
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
就一个BFS算法，应该是简单难度而不是中等难度，这是剑指Offer的老题
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root: return []
        ans = []
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            ans.append(node.val)
        return ans