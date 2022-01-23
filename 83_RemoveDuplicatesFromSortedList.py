'''

Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
Return the linked list sorted as well.

Example 1:

Input: head = [1,1,2]
Output: [1,2]

Example 2:

Input: head = [1,1,2,3,3]
Output: [1,2,3]

Constraints:

    The number of nodes in the list is in the range [0, 300].
    -100 <= Node.val <= 100
    The list is guaranteed to be sorted in ascending order.

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return head


l1 = ListNode(val=1)
l2 = ListNode(val=1)
l3 = ListNode(val=2)
l4 = ListNode(val=3)
l5 = ListNode(val=3)

l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

a = Solution()
#r = a.deleteDuplicates(l1)

while l1.next is not None:
    print(l1.val)
    l1 = l1.next