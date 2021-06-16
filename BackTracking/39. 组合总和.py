'''
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。

重点：begin索引,
    for i in range(begin, size)
    candidates.sort()

'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        n = len(candidates)
        candidates.sort()

        def backTrack(path, begin, size, target):
            if target == 0:
                res.append(path)
                return
            for i in range(begin, size):
                new_target = target - candidates[i]
                if new_target < 0:
                    break
                backTrack(path+[candidates[i]], i, size, new_target)
        
        backTrack(path, 0, n, target)
        return res