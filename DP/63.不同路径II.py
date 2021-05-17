'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
网格中的障碍物和空位置分别用 1 和 0 来表示。
'''

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1: return 0

        '''dp = [[0]*n for _ in range(m)]
        for j in range(n):
            if obstacleGrid[0][j] == 0: dp[0][j] = 1
            else: break
        for i in range(1, m):
            if obstacleGrid[i][0] == 0: dp[i][0] = 1
            else: break
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]'''

        dp = [0]*n
        dp[0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 0 and j-1 >= 0:
                    dp[j] = dp[j] + dp[j-1]
                elif obstacleGrid[i][j] == 1:
                    dp[j] = 0
        return dp[-1]

'''
典型的动态规划加状态压缩
dp[i][j] = dp[i-1][j] + dp[i][j-1]
需要多考虑一个障碍物，所以在动态规划时需要加一个判断
同时需要考虑障碍物在第一行或第一列时，对DP数组的影响
'''