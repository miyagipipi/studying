'''
给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，
计算其二进制数中的 1 的数目并将它们作为数组返回。

官方上一共有3个方法：最高有效位，最低有效位和最低设置位，三者思路不同，但是实际复杂度都一样
方法一需要对每个数遍历其二进制表示的每一位。可以换一个思路，当计算 ii 的「一比特数」时，
如果存在 0 < j< i, j 的「一比特数」已知，且 i 和 j 相比，i 的二进制表示只多了一个 1，
则可以快速得到 ii 的「一比特数」
'''

class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0: return [0]
        dp = [0 for _ in range(num+1)]
        highBit = 0 
        for i in range(1, num+1):
            if i&(i-1) == 0:
                highBit = i    #highBit变量用来维护小于i的最大2的整数幂的值
            dp[i] = dp[i - highBit] + 1
        return dp
'''
对于正整数 xx，将其二进制表示右移一位，等价于将其二进制表示的最低位去掉
由于2//x可以通过i >> 1得到，而x除以2的余数可以通过x&1得到，所以有以下公式
bits[x] = bits[x>>1] + (x&1)
'''
    def countBits(self, num: int) -> List[int]:
        bits = [0]
        for i in range(1, num + 1):
            bits.append(bits[i >> 1] + (i & 1))
        return bits

'''
方法三：最低设置位（x的二进制的最后一个1对应的位数）
y = x&(x-1)，则y为将x的最低设置位从1变成0之后的数，有 y < x
则bits[x] = bits[y] + 1
'''

        bits = [0]
        for i in range(1, num + 1):
            bits.append(bits[i & (i - 1)] + 1)
        return bits