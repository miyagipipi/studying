'''
给定一个二叉树，其中所有的右节点要么是具有兄弟节点（拥有相同父节点的左节点）的叶节点，
要么为空，将此二叉树上下翻转并将它变成一棵树， 原来的右节点将转换成左叶节点。返回新的根。
'''

#解法一：遍历
class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        right = parent = None
        while root:
            left = root.left
            root.left = right
            right = root.right
            root.right = parent
            parent = root
            root = left
        return parent

#解法二：递归
        if root == None or root.left == None:
            return root
        last = self.upsideDownBinaryTree(root.left)
        right = root.right
        root.left.left = right
        root.left.right = root
        root.left = root.right = None
        return last

'''
如果知道怎么翻转一个链表，就知道怎么翻转二叉树
而且这里比较简单一些，不用管树的右子树。
遍历的方法相对简单一下，用三个指针（parent, left, right）
分别维护当前节点，当前节点的左右子节点
也可以不用parent指针，在15行写 root = root.left

递归法相对困难一些，写了很久，还是先写出了翻转链表的递归法，
再依葫芦画瓢改写成功的。
这里有一点要注意的是，我们用last来维护最后一个左节点，
改变每个节点的next的时候（23-26行），尽量保证不要动用last，
因为最终要返回last作为输出结果的根节点。
24-26行就相当于
head.next.next = head
head.next = None
只是多了一个分叉而已。