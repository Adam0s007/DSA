# Given a binary tree root, 
# a node X in the tree is named good if in the path from 
# root to X there are no nodes with a value greater than X.
# Return the number of good nodes in the binary tree.

from collections import deque

 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root) -> int:
        counter = 0
        q = deque()
        if root: q.append((root,root.val))
        while q:
            curr,largest_in_path = q.popleft()
            if curr.val >= largest_in_path:
                counter+=1
                if curr.val > largest_in_path:
                    largest_in_path = curr.val
            if curr.right: q.append((curr.right,largest_in_path))
            if curr.left: q.append((curr.left,largest_in_path))
        return counter