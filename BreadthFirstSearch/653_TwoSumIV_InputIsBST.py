"""

Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

 

Example 1:


Input: root = [5,3,6,2,4,null,7], k = 9
Output: true
Example 2:


Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-104 <= Node.val <= 104
root is guaranteed to be a valid binary search tree.
-105 <= k <= 105

"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        list_of_values = []
        def travel_tree(tree: Optional[TreeNode]):
            if tree is not None:
                nonlocal list_of_values
                list_of_values.append(tree.val)
            
                travel_tree(tree.left)
                travel_tree(tree.right)
        
        travel_tree(root)
        if not list_of_values:
            return False
        
        for i in range(len(list_of_values)):
            for j in range(i + 1, len(list_of_values)):
                if list_of_values[i] + list_of_values[j] == k:
                    return True
        
        return False