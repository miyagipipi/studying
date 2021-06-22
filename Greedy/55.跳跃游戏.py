class Solution:
'''
给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标。
'''
    def canJump(self, nums: List[int]) -> bool:
        target, rightmost = len(nums)-1, 0
        for i in range(len(nums)):
            step = nums[i]
            if i <= rightmost: #小重点
                rightmost = max(rightmost, i+step) #维护rightmost
                if rightmost >= target:
                    return True
        return False

'''
若能到达最后，那么必然存在一个最靠近终点的值能直达终点
（即nums[i]>=k-i),再把最靠近终点的值看为终点（k=i)。
如果能跳跃到最后，则k必然要走到下标为0的元素（即i==1)的
'''
        n = len(nums)
        k = n-1
        for i in range(n-2,-1,-1):
            if i + nums[i]>=k: #当前位置+当前位置允许跳跃的位置 >= 目标（即最后一个位置）
                k=i            #将目标更新为当前位置
        return k==0
