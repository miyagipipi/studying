'''
给定一个 每个结点的值互不相同 的二叉树，和一个目标值 k，找出树中与目标值 k 最近的叶结点。 
这里，与叶结点 最近 表示在二叉树中到达该叶节点需要行进的边数与到达其它叶结点相比最少。
而且，当一个结点没有孩子结点时称其为叶结点。
在下面的例子中，输入的树以逐行的平铺形式表示。
实际上的有根树 root 将以TreeNode对象的形式给出。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distance(self,x0,y0,x1,y1): # 根据两个节点的坐标计算距离
        res = 0
# 如果两个节点不在同一层 首先让layer较大的节点, 即较低的节点上移，变成其父节点
# 对于任意节点，x,y, 其父节点坐标为 x-1,y//2, 相应地，距离+1
        while x0 > x1:                                
            x0 -= 1
            y0 //= 2
            res += 1
        
        while x0 < x1:
            x1 -= 1
            y1 //= 2
            res += 1
        
        while y0 != y1: # 当两节点处于同一层时
# 需要比较其pos, 当pos相等时，两节点即重合,否则两个节点同步上移
# 由于其layer相等，只需考虑pos, 对于任意 pos=y 的节点而言
# 其父节点pos = y//2, # 每次上移，距离+2
            y0 //= 2
            y1 //= 2
            res += 2
        return res

    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        leaf = []                                    # 记录所有叶节点的坐标
        queue = [(0,0,root)]                         # 层序遍历的队列，（0,0）为根的坐标
        x,y = 0,0                                    # 记录目标值所对应坐标

        while queue:
            layer,pos,node = queue.pop(0)            # 队列弹出的值分别为层数、位置和节点
            if node.val == k:                        # 如果找到了坐标值，将其记录下来
                x = layer
                y = pos

            if not node.left and not node.right:      # 如果节点为叶节点
                leaf.append((layer,pos,node.val))     # 记录其坐标和节点值
                continue

            if node.left:                             # 如果节点有左节点
                                                      # 不难想象其坐标值为：
                                                      # layer = layer + 1
                                                      # pos = pos * 2
                queue.append((layer+1,pos*2,node.left))
            
            if node.right:                            # 如果节点有右节点
                                                      # 不难想象其坐标值为：
                                                      # layer = layer + 1
                                                      # pos = pos * 2 + 1
                queue.append((layer+1,pos*2+1,node.right))
                                                    
                                                      # 利用lambda函数和distance
                                                      # 求出距离最小的叶节点
                                                      # 并返回其节点值
        return min(leaf,key=lambda p:self.distance(p[0],p[1],x,y))[2]