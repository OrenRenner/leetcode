'''

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:

Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:

Input: p = [1,2,1], q = [1,1,2]
Output: false



Constraints:

    The number of nodes in both trees is in the range [0, 100].
    -10^4 <= Node.val <= 10^4

'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root1: TreeNode, root2: TreeNode) -> bool:
        tree_vals = []

        def inorder(tree1, tree2) -> bool:
            if tree1 is not None and tree2 is not None:
                if tree1.val == tree2.val:
                    a = inorder(tree1.left, tree2.left)
                    b = inorder(tree1.right, tree2.right)
                    return a and b
                else:
                    return False
            elif (tree1 is None and tree2 is not None) or (tree2 is None and tree1 is not None):
                return False
            else:
                return True

        return inorder(root1, root2)

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        p_val = self.inorderTraversal(p, q)

        return p_val

t1 = TreeNode(val=1)
t1.left = TreeNode(val=1)

t2 = TreeNode(val=1)
t2.right = TreeNode(val=1)

a = Solution()
print(a.isSameTree(t1, t2))