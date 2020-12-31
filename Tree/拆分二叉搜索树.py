#没思路
class Solution:
    def splitBST(self, root: TreeNode, V: int) -> List[TreeNode]:
        if root is None:            #递归基，空
            return None,None
        if root.val == V:           #递归基，恰好分开
            right = root.right
            root.right = None
            return root,right
        if root.val < V:            #当前节点值小于V
            left,right = self.splitBST(root.right,V)
            root.right = left
            return root,right
        if root.val > V:            #当前节点大于V
            left,right = self.splitBST(root.left,V)
            root.left = right
            return left,root