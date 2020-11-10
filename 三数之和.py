'''15.三数之和
'''

'''给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
   使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
'''
#对nums进行从小到大的排序
#令a <= b <= c，则a在nums的前面，c在后面， b在a,c的中间
#如果a确定，则去寻找 b + c = -a的情况
#在确定b的情况下，如果b + c > -a，则让c往前走
#遍历一遍c之后再让b向后走一位
#a 和 b在遍历时都要考虑重复性问题
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        n = len(nums)
        res = []
        nums.sort()
        if n < 3: return res

        for first in range(n-2):
        	#如果a>0，那么a+b+c=0是肯定满足不了的
        	if nums[first] > 0: break
        	if first > 0 and nums[first] == nums[first-1]:
        		continue
        	third = n-1
        	target = -nums[first]
        	for second in range(first+1, n-1):
        		if second > first+1 and nums[second] == nums[second-1]:
        			continue
        		while second < third and nums[second]+nums[third] > target:
        			third -= 1
        		if second == third: break
        		if nums[second] + nums[third] == target:
        			res.append(nums[first], nums[second], nums[third])
        return res