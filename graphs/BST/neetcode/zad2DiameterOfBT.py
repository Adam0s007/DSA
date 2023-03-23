# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        res = [0]
        def dfs(root):
            if not root: return -1
            left = dfs(root.left) #wysokosc w lewym dziecku
            right = dfs(root.right) #wysokosc w prawym dziecku
            res[0] = max(res[0],2 + left + right) # 2 + left + right to srednica!
            return 1 + max(left,right) #zwracamy wysokosc w aktualnym nodzie!
        dfs(root)
        return res[0]
        