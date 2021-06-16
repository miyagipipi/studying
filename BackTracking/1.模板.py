'''
解决一个回溯问题，就是一个决策树的遍历过程
1.路径：当前已作出的选择
2.选择列表：当前可作出的选择
3.结束条件：也就是到达决策树底层时，无法再做出选择时的条件
'''

#伪代码
result = []
def backtrack(path, selectList):
    if not selectList: #可以是满足决策条件的任意代码
        result.append(list(path)) #这里要注意不能直接append
        return

    for select in selectList: #遍历可作出的选择中的所有选择
        path.append(select) #做选择
        
        backtrack(path, selectList) #注意这里path已经改变,
                                    #是否需要改变selectList需要实际考虑
        path.pop() #撤销选择