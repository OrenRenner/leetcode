"""

Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].
Example 2:


Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]
 

Constraints:

The number of nodes in the tree is in the range [1, 10^4].
-2^31 <= Node.val <= 2^31 - 1

"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        sumLevelsList = []
        countLevelsList = []

        def travelTree(tree: Optional[TreeNode], level: int):
            if tree is None:
                return

            nonlocal sumLevelsList
            nonlocal countLevelsList

            if level >= len(sumLevelsList):
                sumLevelsList.append(tree.val)
                countLevelsList.append(1)
            else:
                sumLevelsList[level] += tree.val
                countLevelsList[level] += 1
            
            travelTree(tree.left, level + 1)
            travelTree(tree.right, level + 1)

        level = 0
        travelTree(root, level)

        for idx, item in enumerate(countLevelsList):
            sumLevelsList[idx] /= item

        return sumLevelsList


a = Solution()
a.averageOfLevels(None)