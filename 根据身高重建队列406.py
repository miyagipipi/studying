'''假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，
   其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。 
   编写一个算法来重建这个队列。
   输入:
   [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

   输出:
   [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
'''

'''我的思路:
   创造一个同等长度的list，内部的所有元素都是people中的最大值元素
   people.sort()排序
   开始遍历所有元素，
   count负责记录people当前元素在res中遇到的大于等于h的元素的个数；
   loc负责记录res的当前索引，如line31-34所示
   之后还要判断当前位置是否被其他元素占领了，如果有其他元素，索引+1
   最后把当前元素添加到res的当前索引位置即可

   结果：
   虽然能通过，但是在时间上只超过了13%左右，不是最优化的解法
   没有想到官方解法的逻辑
'''

class Solution(object):
	def reconstructQueue(self, people):
		if not people: return None
        nums = len(people)
        if nums == 1: return people
        people.sort()
        max_peop = max(people)
        res = [max_peop]*nums

        for i in people:
            h, k = i[0], i[1]
            count, loc = 0, 0
            while count < k:
                if h <= res[loc][0]:
                    count += 1
                loc += 1
            while res[loc] != max_peop:
                loc += 1
            res[loc] = [h,k]
        return res

#官方解法
        people.sort(key = lambda x: (-x[0], x[1]))
        output = []
        for p in people:
            output.insert(p[1], p)
        return output
'''我是只用了sort()排序，然后先排最小的，
   去保障最小的之前的k个元素的h都大于等于最小的h即可
   官方是先对people做了更细致的排序--.
   如Line46所示，先按h从大到小排序，再对h相同的元素按k从小到大排序
   使用了list.insert(index, element)方法
'''