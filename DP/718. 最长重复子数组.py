'''
给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
'''

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        '''dp = [[0] * (m + 1) for _ in range(n + 1)]
        ans = 0
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                dp[i][j] = dp[i + 1][j + 1] + 1 if nums1[i] == nums2[j] else 0
                ans = max(ans, dp[i][j])
        return ans'''

        dp = [[0]*(m+1) for _ in range(n+1)]
        res = 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                dp[i][j] = dp[i-1][j-1] + 1 if nums1[i-1] == nums2[j-1] else 0
                res = max(res, dp[i][j])
        return res
'''
dp[i][j]:nums[:i]和nums[:j]中的最大重复子数组的长度
它在nums1[i-1] == nums2[j-1]的情况下等于dp[i-1][j-1] + 1
而如果nums1[i-1] ！= nums2[j-1]，则将它设置为0
用一个res变量来维护每次得到的dp[i][j]和res中的最大值
'''
