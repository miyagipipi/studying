'''

假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:        
        n = len(prices)
        if n == 0: return 0
        
        res = 0
        min_v = prices[0]

        for i in range(1, n):
            res = max(res, prices[i] - min_v)
            min_v = min(min_v, prices[i])
        return res