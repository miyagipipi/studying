'''
给你一个二叉树的根节点 root ，树中每个节点都存放有一个 0 到 9 之间的数字。
每条从根节点到叶节点的路径都代表一个数字：

例如，从根节点到叶节点的路径 1 -> 2 -> 3 表示数字 123 。
计算从根节点到叶节点生成的 所有数字之和 。

叶节点 是指没有子节点的节点。
用变量total来维护当前节点之前得到的总数值
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, preTotal: int) -> int:
            if not root: return 0
            if not root.left and not root.right:
                return preTotal*10 + root.val
            total = preTotal*10 + root.val
            return dfs(root.left, total) + dfs(root.right, total)
        return dfs(root, 0)

    '''
    DFS算法：
    1.用一个字典记录每一层的最左边节点的位置 left{node:pos},
        dict.setdefault(Key, default = None)函数，如果找到Key,
        就返回对应Key的值，如果没有就设置成{Key:default}
    2. 计算最大宽度的方式和BFS一样，用当前节点的pos减去当前层最左节点的pos再+1
    3. 每次进入迭代时，深度都+1，位置区分左右节点
    '''
        ans = 0
        left = {}
        def dfs(node, depth = 0, pos = 0):
            nonlocal ans
            if node:
                left.setdefault(depth, pos)
                ans = max(ans, pos - left[depth] + 1)
                dfs(node.left, depth + 1, pos * 2)
                dfs(node.right, depth + 1, pos * 2 + 1)

        dfs(root)
        return ans