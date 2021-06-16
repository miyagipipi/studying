'''
给定一个二叉树，编写一个函数来获取这个树的最大宽度。树的宽度是所有层中的最大宽度。
这个二叉树与满二叉树（full binary tree）结构相同，但一些节点为空。
每一层的宽度被定义为两个端点（该层最左和最右的非空节点，两端点间的null节点也计入长度）
之间的长度。

思路：
1.如果把每个节点坐标化，然后计算出每层最左和最后节点的位置，并用一个变量来维护最大宽度
    就可以解决这个问题
2.优先BFS算法框架
3.如果根节点坐标算作（0， 0），那么第二层的左节点和右节点分别是（1,1）和（1,2）
    如果某一个节点坐标为（h, i），那么它的左右节点坐标分别为（h+1, i*2），（h+1, i*2+1）
    坐标的第一个元素表示深度，在实际写代码时可以省略
4.因为要经常push 和pop节点，所以这里用deque结构要比list结构更快
'''

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        res = 0
        queue = collections.deque()
        queue.append((root, 0))#queue中的每个元素中，第一个表示节点，第二个表示坐标
        while queue:
            res = max(res, queue[-1][1]-queue[0][1]+1)#就算queue只有一个元素也会计算
            for i in range(len(queue)):
                node, pos = queue.popleft()
                if node.left:
                    queue.append((node.left, pos*2))
                if node.right:
                    queue.append((node.right, pos*2 + 1))
        return res