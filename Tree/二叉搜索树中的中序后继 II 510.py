'''
给定一棵二叉搜索树和其中的一个节点 node ，找到该节点在树中的中序后继。
如果节点没有中序后继，请返回 null 。
一个结点 node 的中序后继是键值比 node.val大所有的结点中键值最小的那个。
你可以直接访问结点，但无法直接访问树。每个节点都会有其父节点的引用。
'''
#我的解法
class Solution(object):
    def inorderSuccessor(self, node):
        #如果node有右孩子，就算Node是其父节点的左孩子，
        #node的右孩子还是比Node大且比node的父节点小
        #在这种情况下，可以不用访问父节点，先进入右孩子，再访问右孩子的左孩子
        #在没有右孩子的情况下，才在父节点上判断：
        #回到父节点上寻找中序后继，

        #遍历node的右子树，不用管左子树
        #注意返回的是节点
        def traversalRightChild(root):
            while root.left:
                root = root.left
            return root
        
        #还需要在父节点上判断（当node没有右子树时），如果node有父节点且node是其父节点的左节点
        #这里有两种选择，一种是什么都不管，直接往上遍历，直到根节点
        #每次都用res = min(root.parent.val, res)
        #第二种是每次遍历父节点时，都考虑当前节点是父节点的左/右子节点
        #这里选择第二种，因为可以不用管节点的值
        def traversalParents(root):
            ans = None
            while root.parent:
                if root.parent.left == root:
                    ans = root.parent
                    return ans
                root = root.parent
            return ans
        if node.right:
            return traversalRightChild(node.right)
        else: return traversalParents(node)

#官方解法
class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        
        # the successor is somewhere upper in the tree
        while node.parent and node == node.parent.right:
            node = node.parent
        return node.parent
'''
官方解法要比我的更简洁
首先把我的两个函数合并在一起了，43行先判断是否有右子树
然后50行的判断也非常巧妙，当前节点是其父节点的右节点时才维持循环
如果不满足循环条件（到根了或者是其父节点的左节点）才返回节点的父节点
'''