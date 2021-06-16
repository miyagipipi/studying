'''
给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，
并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。

中序遍历的前驱节点是当前节点的左节点的一直右节点；
    后驱节点是右节点的一直左节点
但是这里不是通用的前驱后驱节点，因为当当前节点为叶子节点时，
此代码会返回自身节点作为前后节点
所以说，文章中的前驱和后继应该加上限制条件，对于前驱，节点要有左子树；对于后继，节点要有右子树。

'''

class Solution:
    def successor(self, root): #后驱节点值
        """
        One step right and then always left
        """
        root = root.right
        while root.left:
            root = root.left
        return root.val
    
    def predecessor(self, root): #前驱节点值
        """
        One step left and then always right
        """
        root = root.left
        while root.right:
            root = root.right
        return root.val
        
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        
        # delete from the right subtree
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        # delete from the left subtree
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        # delete the current node
        else:
            # the node is a leaf
            if not (root.left or root.right):
                root = None
            # the node is not a leaf and has a right child
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            # the node is not a leaf, has no right child, and has a left child    
            else: #没有右节点且不是叶子节点，则必然有左节点
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
                        
        return root
