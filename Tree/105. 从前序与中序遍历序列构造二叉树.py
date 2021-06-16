'''
根据一棵树的前序遍历与中序遍历构造二叉树。
注意:
你可以假设树中没有重复的元素。
前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回树结构，[3,9,20,null,null,15,7]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        def getTree(leftList: List, rightList: List):
            if not leftList and not rightList: return None
            length = len(leftList)
            if length == 1:
                return TreeNode(leftList[0])
            root = TreeNode(leftList[0])
            index_in_inorder = rightList.index(root.val) #获得root在inorder中的下标

            leftTree_length = index_in_inorder #左子树的长度
            rightTree_length = length - index_in_inorder - 1 #右子树的长度
            if leftTree_length == 0:
                preorder_left, preorder_right = [], leftList[leftTree_length+1 : ]
                inorder_left, inorder_right = [], rightList[index_in_inorder+1 : ]
            elif rightTree_length == 0:
                preorder_left, preorder_right = leftList[1: leftTree_length+1], []
                inorder_left, inorder_right = rightList[0 : index_in_inorder], []
            else:
                preorder_left, preorder_right = leftList[1: leftTree_length+1], leftList[leftTree_length+1 : ]
                inorder_left, inorder_right = rightList[0 : index_in_inorder], rightList[index_in_inorder+1 : ]

            root.left = getTree(preorder_left, inorder_left)
            root.right = getTree(preorder_right, inorder_right)

            return root
        
        n = len(preorder)
        if n == 1: return TreeNode(preorder[0])
        return getTree(preorder, inorder)

'''
以上的代码思路不是最优解，有几个地方还可以优化
首先，我们可以用一个map结构来存贮{元素值：元素下标}，这样就不用每次迭代都去找根节点的下标
即index_in_inorder = rightList.index(root.val)
其次，可以优化下标的处理。即不用每次迭代都对数组进行切片，而是用两个数组对应的下标来代替之
这样在建立root = TreeNode()的时候可以直接用下标来取preorder和inorder对应的元素
'''

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def myBuildTree(preorder_left: int, preorder_right: int, inorder_left: int, inorder_right: int):
            if preorder_left > preorder_right:
                return None
            
            # 前序遍历中的第一个节点就是根节点
            preorder_root = preorder_left
            # 在中序遍历中定位根节点
            inorder_root = index[preorder[preorder_root]]
            
            # 先把根节点建立出来
            root = TreeNode(preorder[preorder_root])
            # 在中序数组中，得到左子树中的节点数目
            size_left_subtree = inorder_root - inorder_left
            # 递归地构造左子树，并连接到根节点
            # 先序遍历中「从 左边界+1 开始的 size_left_subtree」个元素就对应了中序遍历中「从 左边界 开始到 根节点定位-1」的元素
            root.left = myBuildTree(preorder_left + 1, preorder_left + size_left_subtree, inorder_left, inorder_root - 1)
            # 递归地构造右子树，并连接到根节点
            # 先序遍历中「从 左边界+1+左子树节点数目 开始到 右边界」的元素就对应了中序遍历中「从 根节点定位+1 到 右边界」的元素
            root.right = myBuildTree(preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1, inorder_right)
            return root
        
        n = len(preorder)
        # 构造哈希映射，帮助我们快速定位根节点
        index = {element: i for i, element in enumerate(inorder)}
        return myBuildTree(0, n - 1, 0, n - 1)