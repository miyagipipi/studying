'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
'''

#我的解法--回溯算法
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        #需要一个dict来表示数组：字母的映射
        dic = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl',\
                '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        
        n = len(digits)
        selects = [None]*n
        for i in range(n):
            selects[i] = dic[digits[i]]

        path = ''
        res = [] 

        #count表示位数
        def backTrack(path, selects, count):
            #结束条件
            if count == n:
                res.append(str(path))
                return
            for word in selects[count]:
                path += word
                backTrack(path, selects, count+1)
                path = path[:-1]
            return
        backTrack(path, selects, 0)
        return res

#他人解法
#DP
    def letterCombinations(self, digits):
        """
        动态规划
        dp[i]: 前i个字母的所有组合
        由于dp[i]只与dp[i-1]有关,可以使用变量代替列表存储降低空间复杂度
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
             '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        n = len(digits)
        dp = [[] for _ in range(n)]
        dp[0] = [x for x in d[digits[0]]]
        for i in range(1, n):
            dp[i] = [x + y for x in dp[i - 1] for y in d[digits[i]]]
        return dp[-1]

#使用变量res来代替dp[i-1]
        if not digits:
            return []
        d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
             '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        n = len(digits)
        res = ['']
        for i in range(n):
            res = [x + y for x in res for y in d[digits[i]]]
        return res

#递归
        d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
             '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if not digits:
            return []
        if len(digits) == 1:
            return [x for x in d[digits[0]]]
        return [x + y for x in d[digits[0]] for y in self.letterCombinations3(digits[1:])]