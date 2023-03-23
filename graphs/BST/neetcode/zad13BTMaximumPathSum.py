# A path in a binary tree is a sequence of nodes where each pair of 
# adjacent nodes in the sequence has an edge connecting them. 
# A node can only appear in the sequence at most once. 
# Note that the path does not need to pass through the root.

# The path sum of a path is the sum of the node's values in the path.
# Given the root of a binary tree, return the maximum path sum of any non-empty path.

# Definition for a binary tree node.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root) -> int:
        
        def validation(root):
            if not root: return float("-inf")
            maks = max(root.val,validation(root.left),validation(root.right))
            return maks
        maks = validation(root)
        if maks < 0: return maks
        res = [float("-inf")]
        def dfs(root):
            if not root: return 0
            LeftSum = dfs(root.left)
            RightSum = dfs(root.right)
            sumWithSpliting = LeftSum + root.val + RightSum
            res[0] = max(res[0],sumWithSpliting)
            #my musimy zwrocic wyzej maksymalną sumę bez rozdzielania
            sumWithoutSpliting = root.val + max(LeftSum,RightSum)
            if sumWithoutSpliting < 0: sumWithoutSpliting = 0 #to bedzie zwracane dalej!
            res[0] = max(res[0],sumWithoutSpliting)
            return sumWithoutSpliting
        dfs(root)
        return res[0]