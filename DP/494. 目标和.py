'''
思路：
01背包问题是选或者不选，但本题是必须选，是选+还是选-。先将本问题转换为01背包问题。
假设所有符号为+的元素和为x，符号为-的元素和的绝对值是y。
我们想要的 S = 正数和 - 负数和 = x - y
而已知x与y的和是数组总和：x + y = sum
可以求出 x = (S + sum) / 2 = target
也就是我们要从nums数组里选出几个数，令其和为target
于是就转化成了求容量为target的01背包问题 =>要装满容量为target的背包，有几种方案

特例判断
如果S大于sum，不可能实现，返回0
如果x不是整数，也就是S + sum不是偶数，不可能实现，返回0

dp[j]代表的意义：填满容量为j的背包，有dp[j]种方法。
因为填满容量为0的背包有且只有一种方法，所以dp[0] = 1
状态转移：dp[j] = dp[j] + dp[j - num]，
当前填满容量为j的包的方法数 = 之前填满容量为j的包的方法数 + 之前填满容量为j - num的包的方法数
也就是当前数num的加入，可以把之前和为j - num的方法数加入进来。
返回dp[-1]，也就是dp[target]
'''

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        sumAll = sum(nums)
        if S > sumAll or (S + sumAll) % 2:
            return 0
        #转换成求target组合个数的01背包问题
        target = (S + sumAll) // 2

        dp = [0] * (target + 1)
        dp[0] = 1

        for num in nums:
            for j in range(target, num - 1, -1):
                #j从高往低遍历
                dp[j] = dp[j] + dp[j - num]
        return dp[-1]
'''
补充：为什么背包问题是倒着遍历
以此题为例，dp[j] = dp[j] + dp[j - num]
假设这次是第i此遍历， 即dp[i][j] = dp[i-1][j] + dp[i-1][j - num]
等式右边的两项都是存储着第i-1次遍历时的值(即上一次的遍历），
但是因为我们这里对dp进行了状态压缩，省略了i，所以如果我们不倒着遍历
就会存在在计算dp[j]时，dp[j-num]已经被计算（第i遍）的情况，这与不符合我们的算法设计
'''