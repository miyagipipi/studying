#合并区间56
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return None
        n = len(intervals)
        #if n == 1: return [intervals[0]]
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            curr = intervals[i]
            last = res[-1]
            if curr[0] <= last[1]:
                last[1] = max(curr[1], last[1])
            else:
                res.append(curr)
        return res
#给多维数组按某个维度排序的方法：
#array.sort(key = lambda x: x[.][.]...)
