'''276 栅栏涂色
有 k 种颜色的涂料和一个包含 n 个栅栏柱的栅栏，请你按下述规则为栅栏设计涂色方案：

每个栅栏柱可以用其中 一种 颜色进行上色。
相邻的栅栏柱 最多连续两个 颜色相同。
给你两个整数 k 和 n ，返回所有有效的涂色 方案数 。
'''
#dp[i][0]:涂第i个栅栏，且和第i-1个栅栏用的颜色不一样
#dp[i][1]:涂第i个栅栏，且和第i-1个栅栏用的颜色一样

'''状态转移方程：
dp[i][0] = (k-1)*(dp[i-1][0] + dp[i-1][1])
第i-1个栅栏已占用一个颜色，为了使第i个栅栏的颜色和它不同，
则还有k-1个颜色可供选择

dp[i][1] = dp[i-1][0]
在颜色一样的情况下，不影响最终组合数量
'''

class Solution:
    def numWays(self, n: int, k: int) -> int:
    	if not n or not k: return 0
    	dp = [[0, 0] for _ in range(n)]
    	dp[0] = [k, 0]

    	for i in range(1, n):
    		dp[i][0] = (k-1)*sum(dp[i-1])
    		dp[i][1] = dp[i-1][0]
    	return sum(dp[n-1])

   	#可以发现，i仅仅和i-1相关，
   	#所以可以很容易的压缩成常数级空间复杂度
   		if not n or not k: return 0

        diff, same = k, 0
        for i in range(1, n):
            diff, same = (k-1) * (diff + same), diff
        return same + diff
