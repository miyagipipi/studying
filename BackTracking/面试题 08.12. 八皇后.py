'''
重点：
1.棋盘的建立：board = [['.' for _ in range(n)] for _ in range(n)]
2.棋盘在建立时，为了方便替换'Q',首先将每个'.'分割成一个List中的元素
    所以在得到问题的解后，还需要将棋盘中每行每个独立的'.'和'Q'合并
    res.append([''.join(board[i]) for i in range(n)])
注意上述两点的正确代码

3.在check函数中，检查左上角或右上角时，x,y每次循环都要改变
4.在第row行中，可以先不急着将board[row][j] == 'Q',
    而是先检测这个位置放一个Q是否可行，如果可行再放，迭代，回溯

'''
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        res = []

        def check(board, row, col) ->bool:
            #if row == 0: return True
            for i in range(row):
                if board[i][col] == 'Q':
                    return False

            x, y = row -1, col-1
            while x >=0 and y >= 0:
                if board[x][y] == 'Q':
                    return False
                x -= 1
                y -= 1

            x, y = row-1, col+1
            while x >= 0 and y < n:
                if board[x][y] == 'Q':
                    return False
                x -= 1
                y += 1
            return True
        
        def dfs(path, res, row):
            #结束条件：
            if row==n:
                res.append([''.join(board[i]) for i in range(n)] )
                return 
            for j in range(n):
                #path[row][j] = 'Q'
                if check(path, row, j):
                    path[row][j] = 'Q'
                    dfs(path, res, row+1)
                    path[row][j] = '.'
        dfs(board, res, 0)
        return res