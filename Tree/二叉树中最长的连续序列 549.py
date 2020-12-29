'''
给定一个二叉树，你需要找出二叉树中最长的连续序列路径的长度。

请注意，该路径可以是递增的或者是递减。例如，[1,2,3,4] 和 [4,3,2,1] 都被认为是合法的，
而路径 [1,2,4,3] 则不合法。另一方面，路径可以是 子-父-子 顺序，
并不一定是 父-子 顺序。
'''

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        self.ans = 0
        #每次计算的是以当前节点为根节点，能不能组成包含当前节点的连续递增或递减路径
        #所以为了处理可能不含根节点的最长序列，在每次递归完成后需要判断最大值（33行）
        def dfs(root):
            if not root: return [0,0]
            #当前节点自己就能组成长度为1的递增序列或递减序列
            i, d = 1, 1
            l = dfs(root.left)
            r = dfs(root.right)

            if root.left:
                if root.val == root.left.val + 1:
                    i = l[0] + 1
                elif root.val == root.left.val - 1:
                    d = l[1] + 1
            #在处理完左子树后，处理右子树时，最长序列要考虑左子树的影响
            #这样在返回i, d时就是左右子树中的最大值
            if root.right:
                if root.val == root.right.val + 1:
                    i = max(i, r[0] + 1)
                elif root.val == root.right.val - 1:
                    d = max(d, r[1] + 1)
            #i + d计算了两次根节点，所以要减一
            self.ans = max(self.ans, i + d -1)
            return [i, d]
        dfs(root)
        return self.ans