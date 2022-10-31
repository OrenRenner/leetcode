"""

Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

 

Example 1:


Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
Example 2:


Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
 

Constraints:

The number of nodes in the tree is in the range [1, 2 * 104].
1 <= Node.val <= 10^5
1 <= low <= high <= 10^5
All Node.val are unique.

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        rangeSum: int = 0

        def BST(tree: TreeNode):
            nonlocal rangeSum
            if tree is None:
                return
            
            if low <= tree.val <= high:
                rangeSum += tree.val
            
            BST(tree.left)
            BST(tree.right)
        
        BST(root)

        return rangeSum


tree = TreeNode(10)
tree.left = TreeNode(5)
tree.right = TreeNode(15)

tree.left.left = TreeNode(3)
tree.left.right = TreeNode(7)

tree.right.left = TreeNode(13)
tree.right.right = TreeNode(18)

tree.left.left.left = TreeNode(1)
tree.left.right.left = TreeNode(6)

a = Solution()
print(a.rangeSumBST(tree, 6, 10))