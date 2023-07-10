'''

Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.



Example 1:

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:

Input: nums = [1,3]
Output: [3,1]
Explanation: [1,3] and [3,1] are both a height-balanced BSTs.



Constraints:

    1 <= nums.length <= 10^4
    -104 <= nums[i] <= 10^4
    nums is sorted in a strictly increasing order.

Explanation: https://www.youtube.com/watch?v=0K0uCMYq5ng&list=PLot-Xpze53ldg4pN6PfzoJY7KsKcxF1jg&index=5

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list) -> TreeNode:

        def helper(l, r):
            if l > r:
                return None
            else:
                m = (l + r) // 2
                root = TreeNode(nums[m])
                root.left = helper(l, m - 1)
                root.right = helper(m + 1, r)
                return root

        return helper(0, len(nums) - 1)