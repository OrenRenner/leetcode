# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> list:
        tree_vals = []

        def inorder(tree):
            if tree:
                inorder(tree.left)
                tree_vals.append(tree.val)
                inorder(tree.right)

        inorder(root)

        return tree_vals

t = TreeNode(val=2)
t.left = TreeNode(val=3)
t.left.left = TreeNode(val=6)
t.left.right = TreeNode(val=7)

t.right = TreeNode(val=1)
t.right.left = TreeNode(val=6)
t.right.right = TreeNode(val=7)

a = Solution()
print(a.inorderTraversal(t))
