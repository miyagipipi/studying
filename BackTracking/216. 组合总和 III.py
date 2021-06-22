'''
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
说明：
所有数字都是正整数。
解集不能包含重复的组合。

老回溯怪了
'''
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        selects = [i for i in range(1, 10)]
        res = []
        path = []

        def dfs(path:List, res:List, selects:List, begin:int, size:int, k:int, target:int):
            if len(path) == k:
                if target == 0:
                    res.append(list(path))
                return
            
            for i in range(begin, size):
                new_target = target - selects[i]
                if new_target < 0:
                    break
                dfs(path+[selects[i]], res, selects, i+1, size, k, new_target)
        dfs(path, res, selects, 0, 9, k, n)
        return res