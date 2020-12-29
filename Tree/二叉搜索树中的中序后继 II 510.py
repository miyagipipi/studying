'''
给定一棵二叉搜索树和其中的一个节点 node ，找到该节点在树中的中序后继。
如果节点没有中序后继，请返回 null 。
一个结点 node 的中序后继是键值比 node.val大所有的结点中键值最小的那个。
你可以直接访问结点，但无法直接访问树。每个节点都会有其父节点的引用。
'''
class Solution(object):
    def inorderSuccessor(self, node):
        #但是如果node有有孩子，就算Node是其父节点的左孩子，node的右孩子还是比Node大且比node的父节点小
        #在这种情况下，先进入右孩子，再访问右孩子的左孩子
        #在没有右孩子的情况下，才在父节点上判断：（在有父节点的情况下）
        #如果是，则要回到父节点上寻找中序后继，

        #遍历node的右子树，不用管左子树
        #注意返回的是节点！
        def traversalRightChild(root):
            while root.left:
                root = root.left
            return root
        
        #还需要在父节点上判断（当node没有右子树时），如果node有父节点且node是其父节点的左节点
        #这里有两种选择，一种是什么都不管，直接往上遍历，直到根节点
        #第二种是每次遍历父节点时，都考虑当前节点是父节点的左/右子节点
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
        else: return traversalParents(node