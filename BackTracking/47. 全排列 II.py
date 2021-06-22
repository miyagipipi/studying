'''
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
输入：nums = [1,1,2]
输出：[[1,1,2]
      [1,2,1]
      [2,1,1]]
思路：
先排序，再剪枝
由于这里对nums的排序可以从尾到头，所以使用begin来剪枝则不起作用，
则每次的循环迭代都是从头部开始。
可以将结果看成排成一列的箱子，当前箱子的索引为begin，如果begin等于总长度，
就可以将结果返回。
创建一个长度为n的visited数组来，visited[i]的布尔值表示nums[i]是否已经被加入进箱子里。
则在visited[i]==False时才可考虑加入箱子中，但是由于nums中存在重复元素的问题，
所以虽然for i in range(size)每次迭代其实都会重复搜索nums[i]，
但是有一个if not visited[i]加以判断来跳过

还需要考虑去重剪枝的问题。
在not visited[i]的情况下，如果i>0(i==0则nums[i-1]超出索引界限)，且nums[i]==nums[i-1]
(即当前元素和nums前一个元素重复了)，并且not visited[i-1]时，跳过
上面的判断条件，就等于对同父节点的同层，剪枝相同节点
要理解not visted[i-1]，只需要把树结构画出来即可
前面加不加not的区别仅在于保留的是相同元素的顺序索引，还是倒序索引
'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        path =collections.deque()
        nums.sort()
        n = len(nums)
        visited = [False]*n

        def dfs(path, res, begin, size, nums, visited):
            if begin == size:
                res.append(list(path))
                return
            for i in range(size):
                if not visited[i]:
                    if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                        continue
                    path.append(nums[i])
                    visited[i] = True
                    dfs(path, res, begin+1, size, nums, visited)
                    path.pop()
                    visited[i] = False
        
        dfs(path, res, 0, n, nums, visited)
        return res