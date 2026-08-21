# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # bfs - normal algo except swap order of left and right
        # if not root: return None
        # q = deque([root])

        # while q:
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         node.left,node.right = node.right,node.left
        #         q.extend([child for child in [node.left, node.right] if child])
        # return root

        # dfs
        def dfs(root):
            if not root: return None

            root.left,root.right = root.right,root.left
            dfs(root.left)
            dfs(root.right)
            return root

        return dfs(root)
        
