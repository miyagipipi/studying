class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        first, last = None, None

        def dfs(root):
            nonlocal first, last
            if root:
                dfs(root.left)
                if not last:
                    first = root
                else:
                    last.right = root
                    root.left = last
                last = root
                dfs(root.right)
        
        if not root: return None
        dfs(root)
        first.left = last
        last.right = first
        return first