'''给定一个不为空的二叉搜索树和一个目标值 target，请在该二叉搜索树中找到最接近目标值 target 的 k 个值。

注意：

给定的目标值 target 是一个浮点数
你可以默认 k 值永远是有效的，即 k ≤ 总结点数
题目保证该二叉搜索树中只会存在一种 k 个值集合最接近目标值
'''
#我的解法
#中序遍历每个节点，并把各个节点的值加入list结构中
#然后按 abs(root.val - target)的大小顺序排序，取最小的前k个值即可
#时间复杂度为O(n)
class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        res = []
        def dfs(root):
            nonlocal res
            if not root: return
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        return sorted(res, key = lambda x: abs(x - target))[:k]
        
#他人解法
#异曲同工，花里胡哨
        def cur(root):
            return cur(root.left) + [root.val] + cur(root.right) if root else []
        res = sorted(cur(root), key=lambda x: abs(target-x))[:k]    
        return res
#他人解法2
#中序遍历加二分搜索
        tmp = []
        # 先进行中序遍历，得到单调递增数组
        def helper(root):
            if not root:
                return []
            helper(root.left)
            tmp.append(root.val)
            helper(root.right)
        helper(root)
        # 完全变成了最658题找到K个接近的元素
        #假设 mid 是左边界，则当前区间覆盖的范围是 [mid, mid + k -1]. 
        #如果发现 a[mid] 与 x 距离比 a[mid + k] 与 x 的距离要大，说明解一定在右侧。
        n = len(tmp)
        left = 0
        right = n - k
        while left < right:
            mid = left + (right - left) // 2
            if target - tmp[mid] > tmp[mid + k] - target:
                left = mid + 1
            else:
                right = mid
        return tmp[left:left+k]