'''
给定一个二叉树，统计该二叉树数值相同的子树个数。

同值子树是指该子树的所有节点都拥有相同的数值。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        ans = 0
        def dfs(root):
            nonlocal ans
            L, R = [root.val, True], [root.val, True]
            if not root.left and not root.right:
                ans += 1
                return [root.val, True]
            if root.left:
                L = dfs(root.left)
            if root.right:
                R = dfs(root.right)
            if L[0] == R[0] == root.val and L[1] and R[1]:
                ans += 1
                return [root.val, True]
            else:
                return [root.val, False]
        if not root: return ans
        dfs(root)
        return ans
'''
我的解法：
后续遍历，
用17行处理了类似[1, 2, null]的情况（某一边有节点而另一边没有）
但是只返回值是不行的，因为每次比较（25行）都只是和左右两个节点比
没有考虑在子树里面出现不同值的情况（[6,6,6,5])
即并没有判断左右子树是否满足同值子树
于是利用数组结构多返回一个布尔值，用来判断是否满足同值子树
虽然能通过，但不是最优解
'''
#官方解法：
class Solution:
    def countUnivalSubtrees(self, root):
        if root is None: return 0
        self.count = 0
        self.is_uni(root)
        return self.count

    def is_uni(self, node):
        if node.left is None and node.right is None:
            self.count += 1
            return True

        is_uni = True

        if node.left is not None:
            #在判断过程中加入is_uni，是为了防止左不成立而右成立的情况
            is_uni = self.is_uni(node.left) and is_uni and node.left.val == node.val
        if node.right is not None:
            is_uni = self.is_uni(node.right) and is_uni and node.right.val == node.val

        self.count += is_uni
        return is_uni
'''
这里的重点是 True == 1 and False == 0
这个都知道，就没想到还有 1 + True 这种骚操作
之前一直把布尔值看做布尔值，数值看做数值
于是在叶子节点处不用去返回值了，只要返回True即可
然后变量is_uni先设置为True，和我的17行类似
最后再判断左，右子树是否是同值子树

这里要注意一点，在判断时，60行和62行等号的右边加入了is_uni
如果不加它自身，会出现左子树不为同值子树，is_uni == False
右子树为同值子树且值与根节点相同，is_uni == True的错误情况
即is_uni = 子树是否是同值子树 + 当前的is_uni本身是否依然是True + 根节点值与子节点值是否相同
三重判断合一 ---- 逆生三重门

64行是最骚的。
is_uni即做数值，加到self.count中， T就+1， F就+0不变
又做返回的布尔值来判断当前子树是否是同值子树
'''