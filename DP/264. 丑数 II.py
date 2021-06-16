'''
给你一个整数 n ，请你找出并返回第 n 个 丑数 。
丑数 就是只包含质因数 2、3 和/或 5 的正整数。
'''

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        '''factor = [2, 3, 5]
        d = {1}
        heap = [1]

        for i in range(n-1):
            cur = heapq.heappop(heap)
            for x in factor:
                if (nex := cur * x) not in d:
                    heapq.heappush(heap, nex)
                    d.add(nex)
        return heapq.heappop(heap)'''
        
        p2 = p3 = p5 = 1
        dp = [0]*(n+1)
        dp[1] = 1

        for i in range(2, n+1):
            #num2, num3, num5 = dp[p2]*2, dp[p3]*3, dp[p5]*5
            dp[i] = min(num2 := dp[p2]*2, num3 := dp[p3]*3, num5 := dp[p5]*5)  #现学现用海象符
            if dp[i] == num2: p2 += 1
            if dp[i] == num3: p3 += 1
            if dp[i] == num5: p5 += 1
            '''这里用了三个if，而不是if else结构，是因为三个指针存在指向同一个下标的可能'''
        return dp[-1]