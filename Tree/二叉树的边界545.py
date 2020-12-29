'''
给定一棵二叉树，以逆时针顺序从根开始返回其边界。边界按顺序包括左边界、
叶子结点和右边界而不包括重复的结点。 (结点的值可能重复)
左边界的定义是从根到最左侧结点的路径。右边界的定义是从根到最右侧结点的路径。
若根没有左子树或右子树，则根自身就是左边界或右边界。注意该定义只对输入的二叉树有效，而对子树无效。
最左侧结点的定义是：在左子树存在时总是优先访问，如果不存在左子树则访问右子树。
重复以上操作，首先抵达的结点就是最左侧结点。
最右侧结点的定义方式相同，只是将左替换成右。
'''
class Solution(object):
    def __init__(self):
        self.leftSide = []  #左边界上的节点
        self.rightSide = []  #右边界上的节点
        self.leaves = []  #所有叶子节点
    def boundaryOfBinaryTree(self, root):
        #找左边界的函数，注意加入了根节点和最后一个节点
        def findLeftSide(root):
            if root.left:
                self.leftSide.append(root.left.val)
                findLeftSide(root.left)
            elif root.right:
                self.leftSide.append(root.right.val)
                findLeftSide(root.right)
            elif not root.left and not root.right: return
        #找叶子节点
        def findLeaves(root):
            if not root.left and not root.right:
                self.leaves.append(root.val)
            if root.left:
                findLeaves(root.left)
            if root.right:
                findLeaves(root.right)
        #找右边界的函数，注意没有加入根节点
        #找叶子节点中，第一个节点和最后一个节点是对应左边界和右边界各自最后的节点
        def findRightSize(root):
            if root.right:
                self.rightSide.append(root.right.val)
                findRightSize(root.right)
            elif root.left:
                self.rightSide.append(root.left.val)
                findRightSize(root.left)
            elif not root.left and not root.right: return
        #空节点 base case：
        if not root: return []
        #如果只有一个节点的树结构 base case
        if not root.left and not root.right: return [root.val]
        
        #提前判断根节点是否有左子树和右子树，如果有，就调用对应的函数
        self.leftSide.append(root.val)
        if root.left:
            findLeftSide(root)
        if root.right:
            findRightSize(root)
        findLeaves(root)
        #现在，self.leftSide, self.leaves和self.rightSide都被填充了各自的函数
        #其中，leftSide是至少有一个元素（根节点），rightSide有可能是空list，leaves至少有一个根节点（如果只有一个节点的树结构）
        #如果左边界只有一个节点，这个时候不能pop
        if len(self.leftSide) > 1:
            self.leftSide.pop()  #把与第一个叶子节点重复的左边界的lastNode去除，leftSide保证会有一个根节点，所以pop没有问题
        if self.rightSide:
            self.rightSide.pop()  #把与last leave重复的右边界的lastNode去除，右边界不会加入根节点，所以pop的时候要判断是否为空
        self.rightSide.reverse()  #把右边界加入的节点顺序反转
        res = self.leftSide + self.leaves + self.rightSide
        return res