'''
给你一个二叉搜索树和其中的某一个结点，请你找出该结点在树中顺序后继的节点。
结点 p 的后继是值比 p.val 大的结点中键值最小的结点。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        #先找以右子节点为根的子树的最左节点
        #如果没找到，才向上访问父节点
        res = float('inf')
        cur = None
        def findRightNode(root):
            while root.left:
                root = root.left
            return root
        #返回的应该是节点
        #用一个指针cur来标记
        def findParentNode(root):
            nonlocal res, cur
            while root != p:
                if root.val > p.val:
                    cur = root
                    root = root.left
                elif root.val < p.val:
                    root = root.right
        
        if not root: return None
        if p.right:
            res = findRightNode(p.right)
            return res
        else:
            findParentNode(root)
            return cur
'''
14-15行解释了思路
官方解法：中序遍历
如果利用中序遍历把二叉搜索树的节点值都存储进stack
则这个栈一定是递增的
所以利用这一特点可知，节点p的顺序后继就是在这样的
栈中的后一位的节点

直接在中序遍历过程保存前一个访问的节点，
判断前一个节点是否为 p，如果是的话当前节点就是 p 节点的顺序后继。
'''
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        stack = []
        if not root:
            return None
        prev = -math.inf
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if p.val == prev:
                return root
            prev = root.val
            root = root.right
'''
这里是两个while结构
第二个while结构存储当前不为空的节点以及它的非空左节点
61行从stack中取出最后遍历到的左节点
然后do something
prev记录这个节点

可以直接中序遍历搜索，也可以先判断p节点的右子树再中序遍历
前者代码简洁，后者一般耗时少
'''