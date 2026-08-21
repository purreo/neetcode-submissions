# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # iterative dfs is harder
        if not root: return []
        stack = [root]
        res = []
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            stack.extend(c for c in [curr.right,curr.left] if c)
        return res

        # still review recursive dfs