'''
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

一个二叉搜索树的【中序遍历】得到的结果一定是一个升序数组
利用这一特性，我们用一个变量inorder来维护遍历到的最后一个节点值，
然后比较当前节点值和inorder，if inorder >= root.val，则破坏了升序特性

补充：如果这里用队列结构queue代替list结构stack，可以大大提高运行速度
当频繁的增加元素，预留内存空间不够时，python会获取一块更大的内存，并将原list复制后销毁；
同样的，如果不断的减少元素，当元素实际占用内存小于list占用内存一半时，
python也会将list复制到一块更小的内存上，以节省内存的使用
频繁的增加或减少元素，修改list，会导致list在内存中多次的复制，这样就会降低程序的性能
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack, inorder = [], float('-inf')
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # 如果中序遍历得到的节点的值小于等于前一个 inorder，说明不是二叉搜索树
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True