'''
给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。
返回你可以获得的最大乘积。无论如何都要至少拆一次。
'''
class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3: return n-1
        a = n//3
        if (m := n%3) == 0:
            return int(math.pow(3, a))
        elif m == 1:
            return int(math.pow(3, a-1)*4)
        else:
            return int(math.pow(3, a)*2)

'''
数学问题
算术几何均值不等式
一个整数按因素3来等分，等到的乘积最大
其中考虑余数，当余数为1时，要拿出一个3来换成2*2
'''