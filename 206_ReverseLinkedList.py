"""

Given the head of a singly linked list, reverse the list, and return the reversed list.



Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []


Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000


Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        elif head.next.next is None:
            res = head.next
            head.next = None
            res.next = head
            return res
        else:
            last_e = head
            current_e = head.next
            next_e = head.next.next
            last_e.next = None
            while next_e is not None:
                current_e.next = last_e
                last_e = current_e
                current_e = next_e
                next_e = next_e.next
            current_e.next = last_e
            return current_e


l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)

a = Solution()
r = a.reverseList(l)
while r is not None:
    print(r.val)
    r = r.next
