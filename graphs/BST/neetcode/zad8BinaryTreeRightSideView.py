# Given the root of a binary tree, 
# imagine yourself standing on the right side of it, 
# return the values of the nodes you can see ordered from top to bottom.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root):
        ans = []
        q = deque()
        q.append(root)
        while q:
            flag = 1 
            for i in range(len(q)):
                curr = q.popleft()
                # the first node pulled out will be the rightmost one.
                # Then we set the flag and we do not take into account nodes of the same level
                if curr and flag: 
                    ans.append(curr.val)
                    flag = 0  
                if curr:
                    q.append(curr.right) #first we take the right child
                    q.append(curr.left)       
        return ans