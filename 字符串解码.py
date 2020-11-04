'''给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/decode-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def decodeString(self, s):

    	'''我的解法：
    	   能通过，但是耗时较长，而且利用了较多的变量
    	   光是循环就有3个
    	'''

        if not s: return ''
        length = len(s)
        stack = []
        part = ''
        num = ''
        res =''
        
        for i in range(length):
            if s[i] == ']':
                while stack[-1] != '[':
                    part += stack.pop()
                if stack[-1] == '[':
                    stack.pop()
                    while stack and stack[-1].isdigit():
                        num += stack.pop()
                    num = num[::-1]
                    part *= int(num)
                    stack.append(part)
                    part, num = '', ''
            else: stack.append(s[i])
        while stack: res += stack.pop()
        return res[::-1]

        #他人解法
        stack = []  # (str, int) 记录之前的字符串和括号外的上一个数字
        num = 0
        res = ""  # 实时记录当前可以提取出来的字符串
        for c in s:
            if c.isdigit():
            	#这里比我的倒着取再反过来要有效多了
                num = num * 10 + int(c)
            elif c == "[":
                #处理 abc5[...]的情况
                stack.append((res, num))
                res, num = "", 0
            elif c == "]":
                top = stack.pop()
                #最终结果不用再反转一次
                res = top[0] + res * top[1]
            else:
                res += c
        return res

        stack = []
        res = ''
        num = 0
        for i in s:
        	if i.isdigit():
        		num = num*10 + int(i)
        	elif i == '[':
        		stack.append((res, num))
        		res, num = '', 0
        	elif i == ']':
        		part = stack.pop()
        		res = part[0] + res*part[1]
        	else: res += c
        return res