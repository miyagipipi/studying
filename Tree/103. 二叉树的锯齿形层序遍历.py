'''
给定一个二叉树，返回其节点值的锯齿形层序遍历。
（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）

这道题还是考察BFS的算法实现，额外多了一个遍历顺序和一个返回的格式
遍历顺序可以用一个变量order来维护，每次遍历完一层后，order = not order
用一个list结构遍历ans来维护整体的返回，一个queue结构来维护每层节点的值，
完成每层的遍历后，ans.append(list(queue))
这里选择队列的结构而不是数组的结构，更提升整体运行速度
重点在于BFS算法的实现，这个在最后部分给出了代码
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = [root]
        cnt = 0
        while queue:
            cnt += 1
            n = len(queue)
            tmp =[]
            for _ in range(n):
                cur = queue.pop(0)
                tmp.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            if cnt % 2 == 0:
                result.append(tmp[::-1])
            else:
                result.append(tmp)
        return result


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        # 特殊情况处理
        if not root:
            return []        
        # queue 队列先存入根节点
        queue = deque()
        queue.append(root)
        
        # 用来标记当前层是偶数层还是奇数层
        is_even_level = True
        # 结果列表
        ans = []
        
        # 队列不为空时，开始进行遍历
        while queue:
            # 声明双端队列 level_queue
            level_queue = deque()
            # 先计算 queue 的长度 size
            size = len(queue)
            
            # 取出 size 个元素
            for _ in range(size):
                # 取出节点
                node = queue.popleft()
                # 偶数层，将节点值插入到 level_queue 尾部
                if is_even_level:
                    level_queue.append(node.val)
                # 奇数层，将节点值插入到 level_queue 头部
                else:
                    level_queue.appendleft(node.val)
                # 将下一层的节点存放到 queue 中
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # 这里注意，将双端队列转换为列表的形式，存入结果列表中
            ans.append(list(level_queue))
            # 维护更新 is_even_level
            is_even_level = not is_even_level
        
        return ans

def BFS(root):
    if not root: return
    queue = []
    queue.append(root)
    while queue:
        node = queue
        print(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)