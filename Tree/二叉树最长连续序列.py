'''
给你一棵指定的二叉树，请你计算它最长连续序列路径的长度。
该路径，可以是从某个初始结点到树中任意结点，通过「父 - 子」关系连接而产生的任意路径。
这个最长连续的路径，必须从父结点到子结点，反过来是不可以的
'''
#我的解法
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        maxLength = 1
        def dfs(root):
            nonlocal maxLength
            if not root.left and not root.right:
                return 1
            L, R = 1, 1
            if root.left:
                if root.val + 1 == root.left.val:
                    L = 1 + dfs(root.left) #深度遍历不需要这么多if判断
            if root.right:
                if root.val + 1 == root.right.val:
                    R = 1 + dfs(root.right)
            cur = max(L, R)
            maxLength = max(maxLength, cur)
            return cur
        if not root: return 0
        dfs(root)
        return maxLength
'''
如果深度遍历带前提条件（15-16行），那本身就是不完整的遍历
正确做法应该是先遍历完，再来判断
比如官方解法一，就是在遍历完左/右节点后，再来判断，
注意这里是当 当前节点不能和子节点形成连续序列时，将L或R重置为1

或者是解法二，dfs函数的参数除了当前节点外，还记录父节点和长度
先判断当前节点与其父节点是否构成连续序列关系，并更新length和maxLength变量
然后再深度遍历其左右节点
'''
#官方解法
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        maxLength = 0
        def dfs(root):
            nonlocal maxLength
            if not root: return 0
            L = 1 + dfs(root.left)
            R = 1 + dfs(root.right)

            if root.left and root.val != root.left.val - 1:
                L = 1
            if root.right and root.val != root.right.val -1:
                R = 1
            cur = max(L, R)
            maxLength = max(maxLength, cur)
            return cur
        dfs(root)
        return maxLength

#解法二
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        maxLength = 1
        def dfs(root, parent, length):
            nonlocal maxLength
            if not root: return 0
            if parent != None and root.val == parent.val + 1:
                length += 1
            else:
                length = 1
            maxLength = max(maxLength, length)
            dfs(root.left, root, length)
            dfs(root.right, root, length)
        if not root: return 0
        dfs(root, None, 0)
        return maxLength