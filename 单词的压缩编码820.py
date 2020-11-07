'''给定一个单词列表，我们将这个列表编码成一个索引字符串 S 与一个索引列表 A。

   例如，如果这个列表是 ["time", "me", "bell"]，我们就可以将其表示为 S = "time#bell#" 和 indexes = [0, 2, 5]。

   对于每一个索引，我们可以通过从字符串 S 中索引的位置开始读取字符串，直到 "#" 结束，来恢复我们之前的单词列表。

   那么成功对给定单词列表进行编码的最小字符串长度是多少呢？
'''

'''之前一直想怎么给list里面的字符串排序而走不出第一步
   其实list.sort()就会给各个字符串按字母表顺序和长度排好序
'''

'''看到他人的解法是反转+排序后
'''

class Solution(object):
	def minimunLengthEncoding(self, words):
		if len(words) == 1: return len(words[0]) + 1
		for i in range(len(words)):
			words[i] = words[i][::-1]
		words.sort()
		res = 0

		for i in range(len(words) - 1):
			#'me' in 'time' == True
			if words[i+1].startswith(words[i]):continue
			else: res += len(words[i]) + 1
		#这里要注意不管如何都要把最后一个元素的长度加进去，
		#因为上面的遍历没有考虑最后一个元素
		res += len(words[-1]) + 1
		return res

'''补充
   str1.startswith(str2, beg=0,end=len(string));
   方法用于检查字符串1是否是以指定子字符串2开头，
   如果是则返回 True，否则返回 False。
   如果参数 beg 和 end 指定值，则在指定范围内检查。

   line27中不能用in，虽然用in在leecode上能通过且很快
   但是无法解决["me", "met", "mets"]这样的例子
'''