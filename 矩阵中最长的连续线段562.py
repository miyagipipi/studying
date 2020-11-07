#562. 矩阵中最长的连续1线段
'''
    给定一个01矩阵 M，找到矩阵中最长的连续1线段。
    这条线段可以是水平的、垂直的、对角线的或者反对角线的。
'''

class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        row = len(M)
        if row == 0: return 0
        col = len(M[0])
        if col == 0: return 0
        # 水平，坚直，右斜、左斜
        four_d = [[[0, 0, 0, 0] for a in line] for line in M]
        res = 0

        for i in range(row):
            for j in range(col):
                if M[i][j] == 1:
                    if j-1>=0: four_d[i][j][0] = four_d[i][j-1][0] + 1
                    else: four_d[i][j][0] = 1

                    if i-1>=0: four_d[i][j][1] = four_d[i-1][j][1] + 1
                    else: four_d[i][j][1] = 1

                    if i-1>=0 and j-1>=0: four_d[i][j][2] = four_d[i-1][j-1][2] + 1
                    else: four_d[i][j][2] = 1

                    if i-1>=0 and j+1<col: four_d[i][j][3] = four_d[i-1][j+1][3] + 1
                    else: four_d[i][j][3] = 1
                    res = max(res, max(four_d[i][j]))
        return res
