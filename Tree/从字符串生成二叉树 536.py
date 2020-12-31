'''
你需要从一个包括括号和整数的字符串构建一棵二叉树。
输入的字符串代表一棵二叉树。它包括整数和随后的 0 ，1 或 2 对括号。
整数代表根的值，一对括号内表示同样结构的子树。
若存在左子结点，则从左子结点开始构建。
'''

#没做出来.....僵硬
#他人解法
class Solution:
    def str2tree(self, s: str) -> TreeNode:
        if s=="":                              # 当输入字符串为空时，返回None
            return None

        def insert_node(num,stack):            # 插入节点函数，在每次整数输入完成后调用
            node = TreeNode(num)               # 创建以num为值的节点node
            if stack:                          # 如果stack非空，则node节点为栈顶节点的子节点
                if not stack[-1].left:         # 如果栈顶节点没有左子树，node为其左子树
                    stack[-1].left = node
                else:
                    stack[-1].right = node     # 反之，node为其右子树
            stack.append(node)                 # 将node压入栈中
            return [None,1]                    # 返回None和1，分别作为整数num和标志flag的初始值

        num, flag, stack = None, 1, []         # 对num, flag和栈进行初始化

        for c in s:                            # 遍历s中的每一个字符c
            if c == '(':                       # 如果c=='('，且num为数字，插入节点
                if num!=None:
                    num,flag = insert_node(num,stack)
                              
            elif c == ')':
                if num!=None:                  # 如果c==')'，且num为数字，插入节点
                    num,flag = insert_node(num,stack)
                stack.pop()                    # ')'标志着该子树输入完成，因此将其弹出栈

            elif c == '-':                     # 如果有-出现，flag置为-1
                flag = -1
            
            else:                              # 如果c为数字，读入整数
                num = (num*10 + flag*int(c)) if num else flag*int(c)
        
        return stack[0] if stack else TreeNode(num)    # 如果stack非空，返回最顶端的节点，即root
                                                        # 否则返回以num为值的节点