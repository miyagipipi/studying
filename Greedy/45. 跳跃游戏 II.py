'''
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
你的目标是使用最少的跳跃次数到达数组的最后一个位置。
假设你总是可以到达数组的最后一个位置。

在具体的实现中，我们维护当前能够到达的最大下标位置，记为边界。我们从左到右遍历数组，
到达边界时，更新边界并将跳跃次数增加 1。
在遍历数组时，我们不访问最后一个元素，这是因为在访问最后一个元素之前，
我们的边界一定大于等于最后一个位置，否则就无法跳到最后一个位置了。
如果访问最后一个元素，在边界正好为最后一个位置的情况下，我们会增加一次「不必要的跳跃次数」，
因此我们不必访问最后一个元素。
'''
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        rightmost, edge, step = 0, 0, 0
        for i in range(n - 1):
            if rightmost >= i:
                rightmost = max(rightmost, i + nums[i]
                #这一段代码可以保证当右边界包含住最后一个节点时，
                #不必再继续遍历到edge
                if rightmost >= target:
                    step += 1
                    break

                ##一直遍历到edge，动态更新rightmost。到达i到达edge后，更新edge为rightmost
                if i == edge:
                    edge = rightmost
                    step += 1
        return step