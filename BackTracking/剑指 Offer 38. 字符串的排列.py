'''
输入一个字符串，打印出该字符串中字符的所有排列。
你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。
字符串中的字符可以重复出现

用一个变量x来表示当前遍历的索引数，每次遍历s[x:]，并用变量i表示
    然后让c[i]和c[x]互换，并进入x+1迭代，回溯时再将c[i]和c[x]换回来
由于字符可以重复出现，所以必须对重复的路径进行剪枝
    这里使用一个set()结构来存储之前遍历到的字符，而且这个set得放在回溯函数中
'''

class Solution:
    def permutation(self, s: str) -> List[str]:
        c, res = list(s), []
        n = len(c)
        def dfs(x):
            if x == n - 1:
                res.append(''.join(c))   # 添加排列方案
                return
            dic = set()
            for i in range(x, n):
                if c[i] in dic: continue # 重复，因此剪枝
                dic.add(c[i])
                c[i], c[x] = c[x], c[i]  # 交换，将 c[i] 固定在第 x 位
                dfs(x + 1)               # 开启固定第 x + 1 位字符
                c[i], c[x] = c[x], c[i]  # 恢复交换
        dfs(0)
        return res