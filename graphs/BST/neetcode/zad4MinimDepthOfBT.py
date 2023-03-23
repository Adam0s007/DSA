# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# Note: A leaf is a node with no children.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root) -> int:
        def dfs(root):
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if left == 0: return 1 + right #jesli po lewo nie ma liscia, ale po prawej są rozgalezienia, to patrzymy tylko na prawą gałąź!!
            if right == 0: return 1 + left # jesli po prawej nie ma liscia, ale po lewej są rozgałęzienia, to patrzymy tylko na lewą galąź!!
            return 1 + min(left,right)
        return dfs(root)