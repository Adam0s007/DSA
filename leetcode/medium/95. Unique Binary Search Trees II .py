# Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import collections
from typing import List, Optional

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        dp = {}
        def generate(left,right):
            if left > right:
                return [None]
            if (left,right) in dp:
                return dp[(left,right)]
            res = []
            for val in range(left, right + 1):
                
                left_trees = generate(left, val - 1)
                right_trees = generate(val + 1, right)
                for l in left_trees:
                    for r in right_trees:
                        root = TreeNode(val, l,r)
                        res.append(root)
            dp[(left,right)] = res
            return res
        return generate(1,n) if n else []
                