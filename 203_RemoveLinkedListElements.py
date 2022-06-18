'''

Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Example 1:

Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
Example 2:

Input: head = [], val = 1
Output: []
Example 3:

Input: head = [7,7,7,7], val = 7
Output: []


Constraints:

The number of nodes in the list is in the range [0, 104].
1 <= Node.val <= 50
0 <= val <= 50

'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        if head is None:
            return None

        if head.next is None:
            if head.val == val:
                return None
            else:
                return head

        curr = head
        next = head.next
        while curr is not None or next is not None:
            if curr.val == val:
                curr = curr.next
                if curr is None:
                    next = None
                else:
                    next = curr.next
                head = curr
            elif next is not None and next.val == val:
                next = next.next
                curr.next = next
            else:
                curr = curr.next
                if curr is None:
                    next = None
                else:
                    next = next.next

        return head


a = Solution()
lst = ListNode(1)
lst.next = ListNode(1)
lst.next.next = ListNode(1)
# lst.next.next.next = ListNode(3)
# lst.next.next.next.next = ListNode(4)
# lst.next.next.next.next.next = ListNode(5)
# lst.next.next.next.next.next.next = ListNode(6)

new_l = a.removeElements(None, 4)
while new_l is not None:
    print(new_l.val)
    new_l = new_l.next