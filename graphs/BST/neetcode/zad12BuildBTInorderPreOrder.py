# Definition for a binary tree node.
# Given two integer arrays preorder and inorder where preorder is 
# the preorder traversal of a binary tree and inorder is
#  the inorder traversal of the same tree, construct and return the binary tree.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder: return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1],inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])
        # for example: preorder: [3 9 20 15 7]
        #              inorder: [9 3 15 20 7]
        return root
    
    #if it was inorder and postorder:
    #   if len(inorder)==0 or len(postorder)==0:
    #         return None
    #     tree_len = len(postorder)
    #     root = TreeNode(postorder[tree_len -1])
    #     mid = inorder.index(postorder[tree_len -1])
    #     root.left = self.buildTree(inorder[:mid], postorder[:mid])
    #     root.right = self.buildTree(inorder[mid+1:], postorder[mid:tree_len -1])
        
    #     return root