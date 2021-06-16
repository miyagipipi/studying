'''
给定一个二叉树，它的每个结点都存放着一个整数值。
找出路径和等于给定数值的路径总数。
路径不需要从根节点开始，也不需要在叶子节点结束，
但是路径方向必须是向下的（只能从父节点到子节点）。
二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

思路：
1.估计要用回溯算法
2.我们可以用两个数组存储节点和节点值。第一个数组queue形势，每次popleft出的节点表示：
    以当前节点为根节点开始遍历计算路径。
    第二个数组用来存放一条路径上的节点值。
3.用partTarget来动态维护target-node.val的值
4.在以root为节点开始遍历后，每遍历一个节点node，首先判断 node.val <= target
    如果node.val大于target，那肯定不能以node为根节点进行遍历，不用将其pop进queue
    如果node.val <= target，首先pop进queue，然后判断node.val <= partTarget

    如果node.val正好等于partTarget，计数变量count += 1
    如果node.val小于partTarget，part.append(node.val), partTarget -= node.val
    如果node.val大于partTarget,则说明这条路走不通，回溯
然后因为双遍历，时间超时，别人一下就解决了，难受！

'''
# 精简版，五行代码不解释
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def dfs(root, sumlist):
            if root is None: return 0
            sumlist = [num + root.val for num in sumlist] + [root.val]
            return sumlist.count(sum) + dfs(root.left, sumlist) + dfs(root.right, sumlist)
        return dfs(root, [])



# 展开版，易理解
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:

        def dfs(root, sumlist):
            if root is None:
                return 0
            
            sumlist = [num+root.val for num in sumlist]
            sumlist.append(root.val)
            
            count = 0
            for num in sumlist:
                if num == sum:
                    count += 1
            # count = sumlist.count(sum)

            return count + dfs(root.left, sumlist) + dfs(root.right, sumlist)

        return dfs(root, [])