'''
给你一个二进制字符串数组 strs 和两个整数 m 和 n 。
请你找出并返回 strs 的最大子集的大小，该子集中 最多 有 m 个 0 和 n 个 1 。
如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。
'''

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(m+1)]
        for s in strs:
            num0 = num1 = 0
            for num in s:
                if num == '0': num0 += 1
                else: num1 += 1
            
            for i in range(m, num0-1, -1):
                for j in range(n, num1-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-num0][j-num1] + 1)
        return dp[-1][-1]

'''
典型的0-1背包问题，但是这里背包的容量是二维的（即0和1的数量）
背包问题通常都是从后向前遍历
'''