'''
设置函数check(i, j, k)表示判断从网格位置(i, j)出发，能否搜索到单词word[k:]，
如果能，就返回T，否则返回F。check(i, j, k)的执行步骤如下：
    1.if board[i][j] != s[k]：直接返回False
    2.然后判断当前是否已经访问到字符串的末尾，如果是且board[i][j] == s[k]，返回True
    3.如果上述两个判断都不符合，就说明board[i][j] == s[k]且没在末尾，
        然后遍历(i,j)的上下左右位置继续搜索word[k+1:]，
        如果从某个相邻位置出发，能够搜索到word[k+1:]，则返回T，否则返回F

我们对board的每个位置都调用check(i, j, 0)，只要有一处返回T，就能找到

重点：
    因为有重复位置的出现，比如(i, j)是从(i-1, j)垂直下来的，
    那么在继续搜索时就不能再向上搜索了，所以我们需要维护一个与board等大的visited数组，
    用于标识每个位置是否被访问过。并且这个visited在当前层访问结束后，还要清除此位置（即回溯）
注意判断newi, newj是否超出边界 第33行
'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def check(i: int, j: int, k: int) -> bool:
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            
            visited.add((i, j))
            result = False
            for di, dj in directions:
                newi, newj = i + di, j + dj
                if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
                    if (newi, newj) not in visited:
                        if check(newi, newj, k + 1):
                            result = True
                            break
            
            visited.remove((i, j))
            return result

        h, w = len(board), len(board[0])
        visited = set()
        for i in range(h):
            for j in range(w):
                if check(i, j, 0):
                    return True
        
        return False