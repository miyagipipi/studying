'''
给你二叉树的根结点 root ，请你将它展开为一个单链表：
展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，
而左子指针始终为 null 。
展开后的单链表应该与二叉树 先序遍历 顺序相同

简直了
'''

class Solution:
    def flatten(self, root: TreeNode) -> None:
        curr = root
        while curr:
            #if not curr.left，则说明这个节点已经展开完毕，可进入它的右节点进行展开
            if curr.left:
                #因为是先序遍历，所以nxt节点一定是当前节点的左节点
                pre = nxt = curr.left
                while pre.right:
                    pre = pre.right #找到左子树中的最右节点
                pre.right = curr.right #令左子树中的最右节点的右子树 指向 根节点的右子树
                curr.left = None # 置空根节点的左子树
                curr.right = nxt
            curr = curr.right

