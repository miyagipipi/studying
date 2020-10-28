'''5 最长回文子串'''
'''给定一个字符串 s，找到 s 中最长的回文子串'''

#优化解法
def longestPalindrome(self, s):
	if not s: return ""
     length = len(s)
    if length == 1 or s == s[::-1]: return s
        max_len,start = 1,0
    for i in range(1, length):
        even = s[i-max_len:i+1]
        odd = s[i-max_len-1:i+1]
        if i - max_len - 1 >= 0 and odd == odd[::-1]:
            start = i - max_len - 1
            max_len += 2
            continue
        if i - max_len >= 0 and even == even[::-1]:
            start = i - max_len
            max_len += 1
            continue
    return s[start:start + max_len]

#我的解法
	length = len(s)
	if length == 1: return s
	if length == 2: return s if s[0] == s[1] else s[0]
	if s[::] == s[::-1]: return s
	for size in reversed(range(2, length)):
		for loc in range(length - size + 1):
			part = s[loc: loc + size]
			if part == part[::-1]:
				return part
	return s[0]
'''一开始一直在想怎么给回文左右加上相同的数，后面发现
	实现不了，所以没办法写了一个类似于遍历的算法，先是
	看s整体是不是回文，然后遍历查询长度为len(s)-1的子串
	是不是回文，最后一直遍历到长度为2.
	如果找到了，那它肯定是最长的，所以不用再遍历
	如果没有找到，说明没有长度大于1的回文，直接返回s[0]即可'''