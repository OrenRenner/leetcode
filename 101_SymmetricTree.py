'''

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:

Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:

Input: root = [1,2,2,null,3,null,3]
Output: false



Constraints:

    The number of nodes in the tree is in the range [1, 1000].
    -100 <= Node.val <= 100


Follow up: Could you solve it both recursively and iteratively?

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return False
        def compare_children(left: TreeNode, right: TreeNode) -> bool:
            if left is None and right is None:
                return True
            elif left is not None and right is not None:
                if left.val == right.val:
                    return compare_children(left.left, right.right) and compare_children(left.right, right.left)
                else:
                    return False
            else:
                return False

        return compare_children(root.left, root.right)


a = Solution()

root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(2)

root.left.left = TreeNode(3)
root.left.right = TreeNode(4)


root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print(a.isSymmetric(root))
