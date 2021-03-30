'''
对于一棵深度小于 5 的树，可以用一组三位十进制整数来表示。
对于每个整数：
百位上的数字表示这个节点的深度 D，1 <= D <= 4。
十位上的数字表示这个节点在当前层所在的位置 P， 1 <= P <= 8。
位置编号与一棵满二叉树的位置编号相同。
个位上的数字表示这个节点的权值 V，0 <= V <= 9。
给定一个包含三位整数的升序数组，表示一棵深度小于 5 的二叉树，
请你返回从根到所有叶子结点的路径之和。
'''

#我的解法
'''
一开始想用 L_index, R_index = index*2, index*2+1
的特点来利用数组索引代替树结构的left, right
但是测试用例中如果出现[111,217,221,315,415]的情况就无法解决
这是因为测试用例给了深度，位置，所以没有空节点也没有关系，而用
我的想法则必须要加入None去填补空节点才行。
还是构造hash结构更好
'''
class Solution(object):
    def pathSum(self, nums):
        ans = 0
        values = {x // 10: x % 10 for x in nums}
        def dfs(node, running_sum = 0):
            nonlocal ans
            if node not in values: return
            running_sum += values[node]
            depth, pos = divmod(node, 10)
            left = (depth + 1) * 10 + 2 * pos - 1
            right = left + 1

            if left not in values and right not in values:
                ans += running_sum
            else:
                dfs(left, running_sum)
                dfs(right, running_sum)

        dfs(nums[0] // 10)
        return ans