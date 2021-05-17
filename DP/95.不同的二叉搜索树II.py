'''
给定一个整数 n，生成所有由 1 ... n 为节点所组成的 二叉搜索树 。
输入：3
输出：
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n:int):
        def GT(start, end):
            if start > end: return [None]
            #if start == end: return [TreeNode(start)]
            '''如果start == end，表示此时的节点为叶子节点，不应返回None
               而是返回24行所示。如果没有23行，会出现结果没有None的情况'''
            allTree = []

            for i in range(start, end+1):
                #要保证end也能作为根节点，所以这里要end+1
                leftTrees = GT(start, i-1)
                rightTrees = GT(i+1, end)

                for l in leftTrees:
                    for r in rightTrees:
                        currTree = TreeNode(i)
                        currTree.left = l
                        currTree.right = r
                        allTree.append(currTree)
            return allTree

        return GT(1, n) if n else []

'''
这题有思路，但是没写出来，感觉很经典的树结构和递归思维
以i为根节点，则（1~i-1)为左子树，（i+1, n）为右子树
从1~n遍历整个数组（即将1,2，...，n分别作为根节点
再利用递归思维，将（1~i-1)和（i+1, n）带入递归
用一个数组（allTree）来装入每一个二叉树
'''