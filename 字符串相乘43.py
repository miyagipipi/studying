#给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
#不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理
class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        m = len(num1)
        n = len(num2)
        l = [0] * (m+n)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                part = int(num1[i]) * int(num2[j])
                part1 = part % 10
                part2 = part // 10
                l[i+j+1] += part1
                l[i+j] += part2
                if l[i+j+1] >= 10:
                    l[i+j] += l[i+j+1] // 10
                    l[i+j+1] = l[i+j+1] % 10
        res = ''
        #下面这段代码主要是为了解决list中，前面是0的问题，
        #如9998 * 0 和 0*0 等得到的 00000 和 00 的问题
        #这里用一个指针来寻找非0的索引
        i = 0
        while i < len(l) and l[i] == 0:
            i += 1
        for j in l[i:]:
            res += str(j)

        '''上面也可以选择这样的代码，使用字符串的lstrip()方法：
        for i in l:
            res += str(i)
            res = res.lstrip('0')'''
        return res if res else '0'