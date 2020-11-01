#在矩阵中找最大的都为1的正方形
#矩阵中只有'1' and '0'

def findminsqur(matrix):

    #先创造一个内部函数，找到沿当前轴最长的直线
    #如果能正确找到，就改造这个函数，另其分别向下和向右寻找
    rows = len(matrix)
    cols = len(matrix[0])
    maxLength = 0

    def findColLength(matrix, row_nums, col_nums, i, j):
        if i < row_nums and j < col_nums:
            #基本情况
            if matrix[i][j] == 0:
                return 0
            else:
                return findColLength(matrix, row_nums,col_nums, i+1, j) + 1

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                res = findColLength(matrix, rows, cols, i, j)
            maxLength = max(maxLength, res)
    return maxLength
    