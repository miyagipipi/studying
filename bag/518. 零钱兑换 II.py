'''
给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。
假设每一种面额的硬币有无限个
'''

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        dp = [0]*(amount+1)
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]
        return dp[-1]