'''
给定一个整数数组，你需要验证它是否是一个二叉搜索树正确的先序遍历序列。

你可以假定该序列中的数都是不相同的
'''
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        new_min = float('-inf')  # 初始化下限值
        for i in range(len(preorder)):
            if preorder[i] < new_min: return False
            while stack and preorder[i] > stack[-1]:
                new_min = stack.pop()
            stack.append(preorder[i])
        return True

    '''
    如果我们按照前序遍历整个二叉搜索树的值，会得到一个先递减再递增的序列
    如果不满足上述要求（多次递增递减），则必然不满足二叉搜索树特征
    现在我们已经按前序遍历得到这一数组了--preorder -> list
    然后遍历这一数组，用一个辅助栈存储每次遍历的元素
    用一个变量 pre_min 来存在当前最小的元素，此遍历初始化为负无穷大

    这个变量的定义是小于当前元素的所有元素中最大值的那一个元素
    之后的元素都应大于它
    如果值可以重复，这里就通过不了，但是原题中值是不重复的

    当前节点的值大于辅助栈的栈顶元素时，表面序列开始递减，
    这时更新当前最小元素为栈顶元素并弹出栈顶元素。
    循环上述过程直到stack为空或者栈顶元素大于当前节点值
    如果出现当前元素小于当前最小元素，则说明序列出现了递减，则不满是基本要求
    '''