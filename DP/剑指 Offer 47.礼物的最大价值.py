'''
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。
你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、
直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，
请计算你最多能拿到多少价值的礼物？
'''

class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if m == 1: return sum(grid[0])
        '''dp = [[0]*n for _ in range(m)]
        dp[0][0] = grid[0][0]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: continue
                elif i == 0: dp[i][j] = dp[i][j-1] + grid[i][j]
                elif j == 0: dp[i][j] = dp[i-1][j] + grid[i][j]
                else: dp[i][j] = max(dp[i][j-1]+grid[i][j], dp[i-1][j]+grid[i][j])
        return dp[-1][-1]'''

        dp = [x for x in grid[0]]
        for i in range(1,n):
            dp[i] = dp[i] + dp[i-1]
        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    dp[j] = dp[j] + grid[i][j]
                else:
                    dp[j] = max(dp[j-1]+grid[i][j], dp[j]+grid[i][j])
        return dp[-1]