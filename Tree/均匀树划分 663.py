'''
给定一棵有 n 个结点的二叉树，你的任务是检查
是否可以通过去掉树上的一条边将树分成两棵，且这两棵树结点之和相等。
'''
#后续遍历，计算各个子树的和，加入到list中
#最后判断树的和的一半是否存在list中即可
class Solution:
    def checkEqualTree(self, root: TreeNode) -> bool:
        _sum = []
        def getSum(root):
            nonlocal _sum 
            if not root: return 0
            _sum.append(getSum(root.left) + getSum(root.right) + root.val)
            return _sum[-1]
        res = getSum(root)

        #将树的总和去掉
        _sum.pop()
        #注意不是地板除
        return res / 2 in _sum