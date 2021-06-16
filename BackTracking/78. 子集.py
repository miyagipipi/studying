'''
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

思路：
1.定义一个函数helper(i, tmp)，i表示目前的nums索引号，tmp表示当前的子集
2.首先将tmp加入res中，然后遍历寻找nums[i:]之后的索引
    helper(j+1, tmp+[nums[j]]) 将之前的tmp和nums[j]组成新的组合
3. 为什么没有重复：
    因为helper中的for循环是从i开始的
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def helper(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                helper(j+1, tmp+[nums[j]])
        helper(0, [])
        return res