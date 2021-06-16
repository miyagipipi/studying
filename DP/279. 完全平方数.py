'''
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）
使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
给你一个整数 n ，返回和为 n 的完全平方数的 最少数量 。
完全平方数 是一个整数，其值等于另一个整数的平方；
换句话说，其值等于一个整数自乘的积。例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
'''
'''
随着时间的推移，已经提出并证明的数学定理可以解决这个问题
1770 年，Joseph Louis Lagrange证明了一个定理，称为四平方和定理
即每个自然数都可以表示为四个整数平方和：
p = a0^2+a1^2+a2^2+a3^2
四平方定理设置了问题结果的上界(即最多为4个)，但是没有直接告诉我们用最小平方数来分解自然数

在 1797 年，Adrien Marie Legendre用他的三平方定理完成了四平方定理
n != (4^k)(8m+7)的情况下，n=a0^2+a1^2+a2^2
我们可以断言，如果这个数不满足三平方定理的条件，它只能分解成四个平方和

情况 3.1：如果数字本身是一个完全平方数，这很容易检查，例如 n == int(sqrt(n)) ^ 2。
情况 3.2：如果这个数可以分解成两个完全平方数和。不幸的是，
没有任何数学定理可以帮助我们检查这个情况。我们需要使用枚举方法。
'''
class Solution:
    def isSquare(self, n: int) -> bool:
        sq = int(math.sqrt(n))
        return sq*sq == n

    def numSquares(self, n: int) -> int:
        # four-square and three-square theorems
        while (n & 3) == 0:
            n >>= 2      # reducing the 4^k factor from number
        if (n & 7) == 7: # mod 8
            return 4

        if self.isSquare(n):
            return 1
        # check if the number can be decomposed into sum of two squares
        #如果n-i^2的结果是一个完全平方数，则n可以由两个完全平方数组成
        for i in range(1, int(n**(0.5)) + 1):
            if self.isSquare(n - i*i):
                return 2
        # bottom case from the three-square theorem
        return 3