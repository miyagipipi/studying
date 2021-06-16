'''
如果一个数列至少有三个元素，并且任意两个相邻元素之差相同，则称该数列为等差数列。
'''

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3: return 0
        count = 0
        '''left, right = 0, 1
        while right < n:
            d = nums[right] - nums[left]
            while (right+1) < n and nums[right+1] - nums[right] == d:
                right += 1
            now_n = right - left + 1
            count += ((now_n-2)*(now_n-1)) // 2
            left, right = right, right + 1
        return count'''
        res = 0
        for i in range(2, n):
            if nums[i-1]*2 == nums[i-2] + nums[i]:
                count += 1
                res += count
            else:
                count = 0
        return res
'''
两种方法都是数学上的方法
第一种的思路是利用两个指针，找到一组尽可能长度最大的等差数列，
然后通过特定的公式（16行）可以直接算出长度为n的最大等差数列所包含的数量个数
因为有包容关系，所以并不能简单地+1
但是这个方法并不够好，因为有两个指针在数组上滑动，时间复杂度为O(N^2)

方法二利用等差数列的定理公式（21行），来判断等差数列
并且用count变量来记录每次长度+1时额外增加的数列数量
即当（A1~An, d）的总个数为count，长度为n时，若An+1满足21行判断，
则（A1~An+1)比(A1~An)的个数多n-1个，一共有count + n - 1
'''