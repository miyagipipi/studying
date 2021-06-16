'''
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
重点在如何剪枝 for i in range(begin, n-(k-len(path))+2)
'''
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = collections.deque()

        def dfs(path, begin, n, k):
            if len(path) == k:
                res.append(list(path))
                return
            
            for i in range(begin, n-(k-len(path))+2):
                path.append(i)
                dfs(path, i+1, n, k)
                path.pop()
            return
        
        dfs(path, 1, n, k)
        return res