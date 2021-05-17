'''
给定一个二维矩阵，计算其子矩形范围内元素的总和，
该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2)

方法一，先构建一个二维数组DP，存储了matrix数组的每行累加元素值
之后在调用sumRegion函数时，只需要计算每行的self.dp[i][col2] - self.dp[i][col1-1]即可
dp累计和的时间复杂度为O(mn)，检索时为O(m)，仅击败了24%的用户，不是最优解
补充：可以将dp的列数设置为n+1，这样就不需要对col1=0的情况进行特殊处理
'''

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.dp = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                    if j == 0: self.dp[i][j] = matrix[i][j]
                    else: self.dp[i][j] = self.dp[i][j-1] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for i in range(row1, row2+1):
            if col1 == 0: res += self.dp[i][col2]
            else: res += self.dp[i][col2] - self.dp[i][col1-1]
        return res

'''
方法二：二维累计和
_sum[i][j]为矩阵 matrix的以 (i,j)(i,j) 为右下角的子矩阵的元素之和
f(i,j)=f(i−1,j)+f(i,j−1)−f(i−1,j−1)+matrix[i][j]
sumRegion(row1, col1, row2, col2) = 
_sums[row2 + 1][col2 + 1] - _sums[row1][col2 + 1] - _sums[row2 + 1][col1] + _sums[row1][col1]
检索时的时间复杂度为O(1)
_sum数组的长度为m+1行n+1列，能无需处理行或列的下标为0时的特殊情况
'''
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), (len(matrix[0]) if matrix else 0)
        self.sums = [[0] * (n + 1) for _ in range(m + 1)]
        _sums = self.sums

        for i in range(m):
            for j in range(n):
                _sums[i + 1][j + 1] = \
                 _sums[i][j + 1] + _sums[i + 1][j] - _sums[i][j] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        _sums = self.sums
        return _sums[row2 + 1][col2 + 1] - _sums[row1][col2 + 1] - _sums[row2 + 1][col1] + _sums[row1][col1]