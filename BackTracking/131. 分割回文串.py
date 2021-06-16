'''
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
因为是返回所以结果，这样一个穷举过程肯定是用回溯算法

思路：
1.首先利用DP来得到dp[i][j]表示s[i:j+1]是否是个回文
    dp[i][j] = dp[i+1][j-1] and (s[i] == s[j])
2.然后开始回溯
'''

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[True] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            #当i=n-1, j=n时，不会遍历 for j in range(n, n)
            for j in range(i + 1, n):
                dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]

        ret = list()
        ans = list()

        def dfs(i: int):
            if i == n:
                ret.append(list(ans))
                return
            
            for j in range(i, n):
                if dp[i][j]:
                    ans.append(s[i:j+1])
                    dfs(j + 1)
                    ans.pop()

        dfs(0)
        return ret