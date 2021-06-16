'''
输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。
从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

我的思路：
1.遍历所有路径，将每条路径存储。使用先序遍历
2.判断路径和是否等于sum，如果是就加入到最终的返回结果res中，不是则排查
引出的问题：
1.如果求每条路径和，因为某些非叶子节点需要重复计算多次，必然需要用到回溯算法

补充：
在回溯算法中，如果是res.append(path)，这样当path改变时，res中对应的元素也改变，
因为res存储的元素都对应path。需要res.append(list(path))，
相当于额外使用了物理地址来存储一个和path一模一样的数据，并把它加入到res中。

在这里需要进行大量增删的操作时，使用queue结构要比list更快
只要在最后list(queue)即可将queue转换成List结构
'''

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res, path = [], collections.deque()
        def recur(root, tar):
            if not root: return
            path.append(root.val)
            tar -= root.val
            if tar == 0 and not root.left and not root.right:
                res.append(list(path))
            recur(root.left, tar)
            recur(root.right, tar)
            path.pop()

        recur(root, sum)
        return res