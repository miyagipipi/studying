'''
给定一个数组 candidates 和一个目标数 target ，
找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次。

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 

思路：begin确定起始位置，剪枝索引循环
visited判断条件用来剪枝同父节点下同层的重复元素
candidated需要排序
not visited[i]是为了不减去同路径下的重复元素
'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = collections.deque()
        n = len(candidates)
        candidates.sort()
        visited = [False]*n

        def dfs(path, res, begin, size, target,visited):
            if target == 0:
                res.append(list(path))
                return
            
            for i in range(begin, size):
                if not visited[i]:
                    if i > begin and candidates[i] == candidates[i-1] and not visited[i-1]:
                        continue
                    new_target = target - candidates[i]
                    if new_target < 0:
                        break
                    path.append(candidates[i])
                    visited[i] = True
                    dfs(path, res, i+1, size, new_target, visited)
                    path.pop()
                    visited[i] = False
        dfs(path, res, 0, n, target, visited)
        return res