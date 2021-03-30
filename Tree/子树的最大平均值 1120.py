'''
给你一棵二叉树的根节点 root，找出这棵树的 每一棵 子树的 平均值 中的 最大 值。
子树是树中的任意节点和它的所有后代构成的集合。
树的平均值是树中节点值的总和除以节点数。
树中的节点数介于 1 到 5000之间。
每个节点的值介于 0 到 100000 之间。
如果结果与标准答案的误差不超过 10^-5，那么该结果将被视为正确答案。
'''
class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        self._mean = 0

        def findMaxMean(root):
            if not root.left and not root.right:
                self._mean = max(self._mean, root.val)
                return (root.val, 1)

            LSum = LNums = RSum = RNums = 0

            if root.left:
                LSum, LNums = findMaxMean(root.left)
            if root.right:
                RSum, RNums = findMaxMean(root.right)
            thisSum = LSum + RSum + root.val
            thisNums = LNums + RNums + 1
            self._mean = max(self._mean, thisSum / thisNums)
            return (thisSum, thisNums)
        findMaxMean(root)
        return self._mean

'''
就是考察树的深度遍历
这里我选择的是最终遍历到叶子节点（14行），所以必须加18行
（叶子节点的左右为空，则进入不了20-23行的判断，所以提前给变量LSum，LNums，RSum，RNums赋值
还有一种选择是遍历到空节点，这样不用两个if的判断，也可以省略第18行，代码如下

if not root:
	return (0, 0)
LSum, LNums = findMaxMean(root.left)
RSum, RNums = findMaxMean(root.right)
...
整体来说二者在时间复杂度上没有区别
'''