
# Given the root of a binary tree, return the level order traversal of its nodes' 
# values. (i.e., from left to right, level by level).

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root):
        q = deque()
        q.append(root)
        ans = []
        while q:
            level = []
            for i in range(len(q)):
                curr = q.popleft()
                if curr:
                    level.append(curr.val)
                    q.append(curr.left)
                    q.append(curr.right)
            if len(level):
                ans.append(level)
        return ans
        