# Kth Smallest Element in a BST
# Given the root of a binary search tree, and an integer k,
#  return the kth smallest value (1-indexed) of 
#  all the values of the nodes in the tree.

 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root, k: int) -> int:
        index = [0]
        def inorder(root,index):
            if not root: return None
            ans = inorder(root.left,index)
            if ans: return ans
            if index[0] == k-1: return root 
            index[0]+=1
            ans = inorder(root.right,index)
            if ans: return ans
        
        ans = inorder(root,index)
        if ans: return ans.val
    
    #another approach: 
    def kthSmallest1(self, root, k: int) -> int:
        n = 0
        stack = []
        cur = root
        #inorder traversal without recursion & let n be 1-indexed
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()
            n +=1
            if n == k: return cur.val
            cur = cur.right
