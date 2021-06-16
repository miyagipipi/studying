'''
若树 B 是树 A 的子结构，则子结构的根节点可能为树 A 的任意一个节点。
因此，判断树 B 是否是树 A 的子结构，需完成以下两步工作
1.先序遍历树 A 中的每个节点，对应isSubStructure(A,B)函数
2.判断树A 中 以 nA为根节点的子树 是否包含树 B，对应recur(A,B)函数

recur(A,B)终止条件：
1.当节点 B 为空：说明树 B 已匹配完成（越过叶子节点），因此返回 true
2.当节点 A 为空：说明已经越过树 A 叶子节点，即匹配失败，返回 false
3.当节点 A 和 B 的值不同：说明匹配失败，返回 false
    返回值：
如果以上条件都不成立，说明A,B对应节点不为空且二者值相等
1.判断A和B的左子节点，以及二者的右子节点是否相等

isSubStructure(A,B)返回值：
1.以节点A为根节点的子树包含树B，对应recur(A,B)
2.以节点A的左子树包含树B，对应recur(A.left,B)
3.以节点A的右子树包含树B，对应recur(A.right,B)
特殊处理：
    当A或B为空时，直接返回False
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def recur(A, B):
            if not B: return True
            if not A or A.val != B.val: return False
            #如果以上两个判断都不成立，就说明A，B不为空且二者值相等
            #这时候可以递归他们各自的左右节点
            return recur(A.left, B.left) and recur(A.right, B.right)

        return bool(A and B) and (recur(A, B) or \
            self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))