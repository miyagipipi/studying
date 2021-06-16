'''
给你一个整数数组 jobs ，其中 jobs[i] 是完成第 i 项工作要花费的时间。
请你将这些工作分配给 k 位工人。所有工作都应该分配给工人，且每项工作只能分配给一位工人。
工人的 工作时间 是完成分配给他们的所有工作花费时间的总和。
请你设计一套最佳的工作分配方案，使工人的 最大工作时间 得以 最小化 。
返回分配方案中尽可能 最小 的 最大工作时间 。

if groups[i] == 0: break 的解释：
    在某层迭代中，当arr中还有元素并pop出来一个值，但是这个值在groups中的任意位置中放不进去
    即 groups[i] + v > limit。
    在这种情况下，不会进入for循环，而是把这个值重新append进arr并返回False
    于是在它的上层迭代中，if backtrace(arr, groups, limit)返回的是False,
    然后groups[i] -= v
    如果此时groups[i]还不等于0（说明之前放进了其他值）,
    这一层（注意区别）的值v还可以考虑放到groups后面的位置（如果for循环还没有结束的话）
    但是
    如果groups[i] == 0：就说明这个值很大，在groups中任何位置都放不进去，
    因为所有位置的容量都是一样的，这个时候就不用考虑for循环后面的位置能不能放进这个值了
'''
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:

        def check(limit):
            # 剪枝：排序后，大的先拿出来试，如果方案不行，失败得更快
            arr = sorted(jobs)

            groups = [0] * k
            # 分成K 组，看看在这个limit 下 能不能安排完工作
            if backtrace(arr, groups, limit):
                return True
            else:
                return False


        def backtrace(arr, groups, limit):
            # 尝试每种可能性
            #print(arr, groups, limit)
            if not arr: return True #分完，则方案可行
            v = arr.pop()

            for i in range(len(groups)):
                if groups[i] + v <= limit:
                    groups[i] += v
                    if backtrace(arr, groups, limit):
                        return True
                    groups[i] -= v

                    # 如果这个工人分活失败（给他分配这个任务后所有的尝试都是失败的），则剪枝，因为也没必要再往后试了，其他人也会出现一样的情况 
                    if groups[i] ==0:
                        break

            arr.append(v)

            return False
        
        #每个人承担的工作的上限，最小为jos 里面的最大值，最大为 jobs 之和
        l, r  = max(jobs), sum(jobs)

        while l < r:
            mid = (l + r)//2

            if check(mid):
                r = mid
            else:
                l = mid + 1

        return l
