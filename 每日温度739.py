'''请根据每日 气温 列表，重新生成一个列表。
   对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。
   如果气温在这之后都不会升高，请在该位置用 0 来代替。
   例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，
   你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

   提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，
   都是在 [30, 100] 范围内的整数
'''

'''用栈结构，遍历列表每个元素，每次当前元素都去与栈顶元素比较温度
   如果当前温度大于栈顶温度，就pop出栈顶元素，将二者的索引差值加入到
   对应栈顶元素的温度列表的索引的新list中
   最后无论空栈还是其他，都将当前元素push到栈中

   这里我用了(element, index)这样成对地如栈，虽然能通过，
   但是用了更多的时间。事实上，每个element都可以通过它的index
   在温度列表中找到，所以只用push进index即可。
   之前还写了一些if not stack:
   				if stack and T[i] < stack[-1][0]:
   这些都可以删除，因为无论如果当前元素都要入栈
'''

class Solution(object):
    def dailyTemperatures(self, T):
        stack = []
        res = [0]*len(T)

        for i in range(len(T)):
            while stack and T[i] > stack[-1][0]:
                tem_last = stack.pop()
                res[tem_last[1]] = (i - tem_last[1])
            stack.append( (T[i], i) )
        return res

        #官方解法
        length = len(T)
        ans = [0] * length
        stack = []
        for i in range(length):
            temperature = T[i]
            while stack and temperature > T[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index
            stack.append(i)
        return ans
