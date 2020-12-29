class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        res = []
        
        def dfs(root):
            nonlocal part, leave
            if not root.left and not root.right:
                leave = root #标记叶子节点
                part.append(root.val)

            if root.left: dfs(root.left)
            if root.left == leave: root.left = None

            if root.right: dfs(root.right)
            if root.right == leave: root.right = None
            return root
            
        if not root: return []
        if not root.right and not root.left: return [[root.val]]
        while root:
            leave = None
            part = []
            root = dfs(root)
            res.append(part)
            if not root.left and not root.right:
                res.append([root.val])
                break
        return res
'''
以上是我的解法，深度遍历，每次都找到并标记叶子节点
然后令叶父节点的指向标记了的叶子节点（left or right）为None
用20行的循环来遍历树，直到仅剩根节点
这里会出现两个问题：
1.当树被剪切成仅剩根节点时，会出现死循环，所以加了25-27行来break
2.1无法解决树本身就仅有一个节点的问题，所以又在循环外加了一个判断 19行
虽然能通过，但这样肯定不是最优解，时间复杂度O(n2)
'''

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        res = []

        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            height = max(left, right) #当前节点的高度
            if len(res) == height:
                res.append([])
            res[height].append(root.val)
            return height + 1
        helper(root)
        return res
            
'''
优化的解发现输出的结果都是通过利用叶子节点的高度相同这一点来进行访问的
且输出结果的索引正好应对高度递增（高度为0的叶子节点一组，高度为1一组
高度为2一组，......直到根节点
这样只用遍历一次树就完成了，时间复杂度O(n)
遍历顺序为后续遍历
'''