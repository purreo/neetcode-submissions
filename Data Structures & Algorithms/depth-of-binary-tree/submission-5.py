# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # bfs
        if not root: return 0
        q = deque([(root,1)])
        maxd = 0
        while q:
            for r in range(len(q)):
                node,level = q.popleft()
                maxd = max(maxd,level)

                if node.left: q.append((node.left, level + 1))
                if node.right: q.append((node.right, level + 1))
           
        return maxd