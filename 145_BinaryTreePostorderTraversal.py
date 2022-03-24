'''

Given the root of a binary tree, return the postorder traversal of its nodes' values.



Example 1:


Input: root = [1,null,2,3]
Output: [3,2,1]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]


Constraints:

The number of the nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100


Follow up: Recursive solution is trivial, could you do it iteratively?

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> list:
        post_order, stack = [], []
        prev, p = None, root
        while stack or p:
            if p:
                stack.append(p)
                p = p.left
            else:
                top = stack[-1]
                if top.right and top.right != prev:
                    p = top.right
                else:
                    post_order.append(top.val)
                    prev = top
                    stack.pop()
        return post_order