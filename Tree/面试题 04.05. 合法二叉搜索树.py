'''
实现一个函数，检查一棵二叉树是否为二叉搜索树。

思路：
中序遍历，比较当前节点值和中序遍历中，当前节点的前一个值（即最新遍历到的值）
如果当前节点值小于前节点值，必然不满足二叉搜索树
如果当前节点值大于前节点值，则继续遍历节点
可以选择循环和迭代两种方法：
循环的话，需要一个stack来存放节点，还需要一个inorder变量来维护前一个节点的值
迭代的话，不需要stack存放节点，但是需要lower和upper两个参数
'''
#Definition for a binary tree node.
 class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def isValidBST(self, root):
        stack = collections.deque()
        inorder = float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        return True