'''
给定一个二叉树，找到其中最大的二叉搜索树（BST）子树，并返回该子树的大小。
其中，最大指的是子树节点数最多的。
二叉搜索树（BST）中的所有节点都具备以下属性：
左子树的值小于其父（根）节点的值。
右子树的值大于其父（根）节点的值。
'''

'''
没做出来.....
它需要维护很多变量
'''

class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        
        def dfs(root):
            if not root: return float('inf'), float('-inf'), 0
            L_min, L_max, lv = dfs(root.left)
            R_min, R_max, rv = dfs(root.right)
            if L_max < root.val < R_min:
                return min(L_min, root.val), max(R_max, root.val), lv + rv + 1
            return float('-inf'), float('inf'), max(lv, rv)
        res = dfs(root)[2]
        return res

#重点在22行，23行
#如果需要维护很多变量，例如本题需要知道左子树中的最小值，最大值和满足BST的节点总数
#以及右子树的最小值，最大值和满是BST的节点总数，可以直接返回一个数组