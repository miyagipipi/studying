'''
给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。

重点：
子集都是树结构的遍历问题，都会引申出剪枝和去重的问题
剪枝的问题一般是用一个begin索引， 如for i in range(begin, len(nums))
    剪枝问题可以解释为不再考虑索nums中索引小于begin的数进行组合
去重分两种，第一种为同枝去重，即[1, 2, 2]是不符合的
        第二种是同一父节点下的同层去重，如本题
        第一种可以用一个visited数组来存放同枝重复的元素并注意回溯
        第二种就是如24行所示的代码逻辑：
            在同层中（dfs函数下的for i in range(begin, len(nums))就是同层逻辑）
            如果
'''
class Solution(object):
    def subsetsWithDup(self, nums):
        res, path = [], []
        nums.sort()
        self.dfs(nums, 0, res, path)
        return res
        
    def dfs(self, nums, begin, res, path):
        res.append(list(path))
        for i in range(begin, len(nums)):
            if i > begin and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            self.dfs(nums, i + 1, res, path)
            path.pop()