#在矩阵中找最大的都为1的正方形
#矩阵中只有'1' and '0'

class Solution(object):
	def maximalSquare(self, matrix):
	   	#我的想法：遍历每个元素，如果它为1则正方形尺寸+1
	   	#然后考虑它的下方，右方和右下对角线的三个元素
	   	#如果这三个都为1， 就递归函数
	   	#还没做出来.....僵硬，看了力扣的官方解法，哎
		if not matrix: return 0
        rows = len(matrix)
        cols = len(matrix[0])
        maxLength = 0

        def findMaxLength(matrix, row_nums, col_nums, i, j):
            if i < row_nums and j < col_nums:
                if matrix[i][j] == '1':
                    if i+1 < row_nums and j+1 < col_nums and matrix[i+1][j] == '1' and matrix[i][j+1] == '1' and matrix[i+1][j+1] == '1':
                        a = findMaxLength(matrix, row_nums, col_nums, i+1, j)[0] + 1
                        b = findMaxLength(matrix, row_nums, col_nums, i, j+1)[1] + 1
                        return (a, b)
                    else: return (1, 1)
            else: return (0, 0)
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    res, res2 = findMaxLength(matrix, rows, cols, i, j)
                    res3 = min(res, res2)
                    maxLength = max(maxLength, res3)
                else: continue
                
        return maxLength*maxLength

    #官方解法：
    '''用 dp(i, j) 表示以 (i,j) 为右下角，且只包含 1 的正方形的边长最大值。
       如果该位置的值是 0，则 dp(i, j) = 0，
       因为当前位置不可能在由 11 组成的正方形中；
	   如果该位置的值是 1，则 dp(i, j)的值由其上方、左方
	   和左上方的三个相邻位置的 dp 值决定。
	   具体而言，当前位置的元素值等于三个相邻位置的
	   元素中的最小值加 1
	   此外，还需要考虑边界条件。如果 i 和 j 中至少有一个为 0，
	   则以位置 (i, j) 为右下角的最大正方形的边长只能是 1，因此 dp(i, j) = 1
	'''
	if len(matrix) == 0 or len(matrix[0]) == 0:
		return 0
	maxSide = 0
	rows, columns = len(matrix), len(matrix[0])
	dp = [ [0] * columns for _ in range(rows)]

	for i in range(rows):
		for j in range(columns):
			if matrix[i][j] == '1':
				if i == 0 or j == 0:
					dp[i][j] == 1
				else:
					dp[i][j] = max(dp[i-1][j], dp[i][j-1],
						dp[i-1][j-1]) + 1
				maxSide = max(maxSide, dp[i][j])
	maxSquare = maxSide*maxSide
	return maxSquare