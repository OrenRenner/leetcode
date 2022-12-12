"""

Given the root of a Binary Search Tree (BST), return the minimum difference between the values of any two different nodes in the tree.

 

Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 100].
0 <= Node.val <= 105

"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        value_list = []

        def get_val(tree: Optional[TreeNode]):
            nonlocal value_list
            if tree is not None:
                value_list.append(tree.val)
                get_val(tree.left)
                get_val(tree.right)
        
        get_val(root)
        min_diff = abs(value_list[1] - value_list[0])
        for i in range(len(value_list)-1):
            for j in range(i+1, len(value_list)):
                min_diff = min(min_diff,
                               abs(value_list[j]-value_list[i]))
        return min_diff
