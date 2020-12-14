'''
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        d = dict()
        d[0] = 1
        ans = 0
        sum_i = 0
        for i in nums:
            sum_i += i
            sum_j = sum_i - k
            if sum_j in d:
                ans += d[sum_j]
            if sum_i in d:
                d[sum_i] += 1
            else: d[sum_i] = 1
        return ans

'''
解释:
    使用了哈希表结构，此结构主要起两个作用
    1.仅存储前缀和sums[i]的值（key）和前缀和出现的次数（value）】
    2.在每次遍历过程中，询问sums[j]是否在此哈希表中

    而sums[j]用 sums[i] - k 代替，即14行所示
    这样，如果sums[i] - k的值在哈希表中存在，就代表之前有一前缀和sums[j]，
    满足sums[i] - sums[j] == k成立，即nums[i+1:j]之和为k，然后更新ans

    这里说明一下为什么要提前存储{0:1}(9行所示)
        如果正好有sum(nums[ : i+1]) 的值等于k，且是第一次出现
        即sums[i] - k == 0，那么满足要求，ans需要加1
        但是这个时候，哈希表中没有存储这一键值对，
        会在询问 0 是否在哈希表中时得到false。
'''