'''

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.



Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5



Constraints:

    The number of nodes in the tree is in the range [0, 10^5].
    -1000 <= Node.val <= 1000

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:

        def counter_depth(tree: TreeNode) -> int:
            count = 1
            left = 0
            right = 0

            if tree is None:
                return 0

            if tree.left is not None:
                left = counter_depth(tree.left)
            if tree.right is not None:
                right = counter_depth(tree.right)

            if left == 0 or right == 0:
                count += max(left, right)
            else:
                count += min(left, right)

            return count

        return counter_depth(root)


a = TreeNode(3)
a.left = TreeNode(9)
a.right = TreeNode(20)
a.right.left = TreeNode(15)
a.right.right = TreeNode(10)

s = Solution()
print(s.minDepth(a))