# Given a binary tree, determine if it is height-balanced.
# For this problem, a height-balanced binary tree is defined as:
# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root) -> bool:
        def dfs(root):
            if not root: return -1,True
            left,ans1 = dfs(root.left)
            right,ans2 = dfs(root.right)
            if not ans1 or not ans2: return 0,False
            if abs(left-right) > 1: return 0,False 
            return 1 + max(left,right),True
        heigh,ans = dfs(root)
        return ans