# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # dfs
        # def dfs(root):
        #     if not root: return 0
        #     return max(dfs(root.left) + 1,dfs(root.right) + 1)
        #     return height
            
        # return max(0,dfs(root))

        #bfs - store depth on q
        if not root: return 0
        q = deque([[root,1]])
        max_depth = 0
        while q:
            node,depth = q.popleft()
            max_depth = max(max_depth,depth)
            if node.left:
                q.append([node.left,depth + 1])
            if node.right:
                q.append([node.right,depth + 1])

        return max_depth



