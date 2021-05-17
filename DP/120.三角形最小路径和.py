'''
给定一个三角形 triangle ，找出自顶向下的最小路径和。
每一步只能移动到下一行中相邻的结点上。相邻的结点
在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1

这是1994 年的 IOI（国际信息学奥林匹克竞赛）的 The Triangle题
现在已经是动态规划的入门必做题目
'''

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        layer = len(triangle)   #第n层则有n个元素
        if layer == 1: return triangle[0][0]
        dp = [[0]*layer for _ in range(layer)]
        dp[0][0] = triangle[0][0]

        for i in range(1, layer):
            for j in range(i+1):
                if j == 0:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                elif j == i:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j]+triangle[i][j], dp[i-1][j-1]+triangle[i][j])
        return min(dp[-1])
        '''
        方法一是典型的动态规划，时间复杂度和其他方法一样，但是空间复杂度是O(n^2)
        '''

        dp = [0]*layer
        dp[0] = triangle[0][0]
        #cur = 0  
        for i in range(1, layer):
            #pre_num = dp[cur]
            pre_num = dp[0]
            for j in range(i+1):
                if j == 0:
                    dp[j] = dp[j] + triangle[i][j]
                elif j == i:
                    dp[j] = pre_num + triangle[i][j]
                    #cur = 0
                else:
                    dp[j], pre_num = min(pre_num + triangle[i][j], dp[j] + triangle[i][j]), dp[j]
                    #cur += 1
                    #pre_num = dp[cur]
        return min(dp)
        '''
        方法二对dp数组进行了状态压缩，空间复杂度为O(n)
        '''

        n = len(triangle)
        f = [0] * n
        f[0] = triangle[0][0]

        for i in range(1, n):
            f[i] = f[i - 1] + triangle[i][i]
            for j in range(i - 1, 0, -1):
                f[j] = min(f[j - 1], f[j]) + triangle[i][j]
            f[0] += triangle[i][0]
        
        return min(f)
        #这是官方题解，感觉还是方法二更清晰明了一些，方法三的58-59行不好理解