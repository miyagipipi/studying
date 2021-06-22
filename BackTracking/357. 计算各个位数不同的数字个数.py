'''
给定一个非负整数 n，计算各位数字都不同的数字 x 的个数，其中 0 ≤ x < 10n 
思路：
1.典型的回溯算法，这里用visited数组来存储重复元素，
    用一个size参数来解决首位是0的问题
'''
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        count = 10
        path = 0
        visited = []

        def dfs(path, visited, size):
            nonlocal count
            #结束条件
            if 9 < path < 10**n:
                count += 1
            
            for num in range(10):
                if num not in visited:
                    path = path*10 + num
                    if path >= 10**n:
                        break
                    if path == 0 and size == 1:
                        continue
                    visited.append(num)
                    dfs(path, visited, size+1)
                    path = path // 10
                    visited.pop()
            return
        
        if n == 0: return 1
        if n == 1: return 10
        dfs(path, visited, 1)
        return count

#方法二 DP+回溯
        def dfs(path:List, nums:List, size:int):
            if len(path) == size:
                nonlocal count
                count += 1
                return
            for j in range(len(nums)):
                if not path and nums[j] == 0:
                    continue
                path.append(nums[j])
                dfs(path, nums[:j]+nums[j+1:], size)
                path.pop()
            return
        
        if n == 0: return 1
        if n == 1: return 10
        
        nums = [i for i in range(10)]
        dp = [0 for _ in range(n+1)]
        dp[0],dp[1] = 1, 10
        
        for i in range(2, n+1):
            count = 0
            dfs([], nums, i)
            dp[i] = dp[i-1] + count
        return dp[-1]