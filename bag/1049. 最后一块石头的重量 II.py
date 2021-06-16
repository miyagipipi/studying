'''
有一堆石头，用整数数组 stones 表示。其中 stones[i] 表示第 i 块石头的重量。
每一回合，从中选出任意两块石头，然后将它们一起粉碎。
假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：
如果 x == y，那么两块石头都会被完全粉碎；
如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
最后，最多只会剩下一块 石头。返回此石头 最小的可能重量 。如果没有石头剩下，就返回 0。

思路：
1.总重量Weight = sum(stones)
    如果能完全粉碎，则Weight为偶数且两组石头的总量都是 Weight/2
    就算不能完全粉碎，也应该使其中一组石头的重量尽可能接近 Weight/2
2.令target = Weight//2
    若stones中能选取一组石头，使其重量在其他选择中是最大的（在小于 target的情况下）
    如果这组石头的重量为a，则所求的结果为(Weight-a) - a
3.至此，转换成了背包问题
    dp[i+1][j]表示从stones[:i+1]中（即前i个石头）能否选出一组重量为j的石头组合
    设stones长度为n，我们最终想要获得dp[n][target]（如果可以）
    所以dp数组为n+1行，target+1列（不然取不到[n][target]下标）
4.状态压缩
    i+1只和i有关，可以压缩。然后注意需要倒着遍历
'''
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        n = len(stones)
        target = total // 2
        dp = [False] * (target+1)
        dp[0] = True

        for stone in stones:
            for j in range(target, stone-1, -1):
                dp[j] = dp[j] or dp[j-stone]
        
        ans = float('inf')
        for j in range(target, -1, -1):
            if dp[j]:
                ans = min(ans, total - 2*j)
        return int(ans)



        total = sum(stones)
        n = len(stones)
        target = total // 2
        dp = [[False]*(target+1) for _ in range(n+1)]
        dp[0][0] = True

        for i in range(n):
            for j in range(target + 1):
                if j < stones[i]:
                    dp[i + 1][j] = dp[i][j]
                else:
                    dp[i + 1][j] = dp[i][j] or dp[i][j - stones[i]]
        
        res= 0
        for j in range(target, -1, -1):
            if dp[-1][j] == True:
                res = total - 2*j
                break
        return res