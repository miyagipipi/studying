'''
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先

Copy from Krahets
最近公共祖先的定义：
设节点 root 为节点 p, q 的某公共祖先，
若其左子节点 root.left 和右子节点 root.right 都不是 p,q 的公共祖先，
则称 root 是 “最近的公共祖先”
所以如果root是节点p, q的最近公共祖先节点的话，无非两种情况：
1.p, q分别在root的两侧
2.p, q中有一个节点为root，且另一个在其左或右子树中

考虑通过递归对二叉树进行后序遍历，当遇到节点 p 或 q 时返回。
从底至顶回溯，当节点p,q在节点 root 的异侧时，节点 root 即为最近公共祖先，
则向上返回 root
终止条件：
1.当越过叶子节点后，返回null
2.当root == p or q时，返回root

递归工作：
1.递归左节点，标记返回值为left
2.递归右节点，标记返回值为right
返回值：
1.当left, right同时为空时，说明root的左右子树都不包含p, q，所以返回null
2.当left, right都不为空时，说明p, q正好在root的两侧，因此此时root为最近的公共祖先，返回root
3.当left, right有一个为空，另一个不为空时，返回不为空的那一个
    设left为空，right不为空，则p, q都在root的右子树中，这时有两种情况：
    1.两个节点都在root的右子树中，所以此时root为两节点的最近公共祖先节点，返回right
    2.p, q中有一个在root的右子树中，而另一个就是root，也返回right

思路和代码都很精彩
'''

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left: return right
        if not right: return left
        return root