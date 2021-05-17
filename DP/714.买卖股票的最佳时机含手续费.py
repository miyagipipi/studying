'''
给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；
非负整数 fee 代表了交易股票的手续费用。
你可以无限次地完成交易，但是你每笔交易都需要付手续费。
如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
返回获得利润的最大值。
注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。
'''

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        '''days = len(prices)
        dp = [[0,0,0] for _ in range(days)]
        dp[0][0] = -prices[0]

        for i in range(1, days):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]-prices[i], dp[i-1][2]-prices[i])
            dp[i][1] = dp[i-1][0] + prices[i] - fee
            dp[i][2] = max(dp[i-1][1], dp[i-1][2])
        return max(dp[-1][1], dp[-1][2])'''

        dp = [-prices[0], 0, 0]
        for price in prices:
            cur0, cur1, cur2 = dp[0], dp[1], dp[2]
            dp[0] = max(cur0, cur1-price, cur2-price)
            dp[1] = cur0 + price - fee
            dp[2] = max(cur1, cur2)
        return max(dp[1], dp[2])

        p0, p1 = 0, -prices[0]
        for price in prices:
            cur0, cur1 = p0, p1
            p0 = max(cur0, cur1 + price - fee)
            p1 = max(cur1, cur0 - price)
        return max(p0, p1)
'''
经典的动态规划+状态压缩
甚至在状态压缩中都不需要list结构，用以下三个变量代替即可
p0, p1, p2 = -prices[0], 0, 0
还可以压缩成两个状态！
'''