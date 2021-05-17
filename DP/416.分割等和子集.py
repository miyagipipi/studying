'''
给你一个 只包含正整数 的 非空 数组 nums 。
请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等

先处理一些肯定不能分割的情况：数组长度为1， 数组总和为奇数，数组中最大的数大于总和的一半
本题是NP完全问题，无多项式算法
可以将这个问题转换为0-1背包问题，但是这道题要求选取的数字的和恰好等于整个数组的一半
DP数组n行target+1列，
dp[i][j]:从数组[0:i]下标范围内选择若干个正整数（可以选0个），
是否存在一种选取方案，使得被选取的值的和等于j，若等于，则dp[i][j] = True
边界：dp[i][0] = True(都不选)，dp[0][nums[0]] = True（只有nums[0]可选）

状态转移方程：
    如果nums[i] > j:这个时候nums[i]就不能被选取，所以dp[i][j] = dp[i-1][j]
    如果nums[i] <= j:这个时候nums[i]可选可不选
        所以dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
        解释一下，等式右边第一项表示不选nums[j]的情况，则在i-1的位置就有总和等于j的解决方案
        第二项表示选了nums[i]的情况，它等于之前的总和正好等于j-nums[i]，选取了nums[i]之后
        总和正好为j
'''

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1: return False

        sum_v = sum(nums)
        max_v = max(nums)
        
        if sum_v % 2 == 1: return False
        target = sum_v // 2
        if max_v > target: return False

        dp = [[False for _ in range(target+1)] for _ in range(n)]
        for i in range(n):
            dp[i][0] = True
        dp[0][nums[0]] = True

        for i in range(1, n):
            num = nums[i]
            for j in range(1, target+1):
                if num > j:
                    dp[i][j] = dp[i-1][j]
                elif num <= j:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-num]
        return dp[n-1][target]

'''
两个注意点：
1.列的数量一共是target+1列，这样最后一列的下标才是target
2.行的数量不是n+1行，因为其下标要和nums一致
'''