'''

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.



Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]



Constraints:

    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return None

        l3 = ListNode(val=None)
        tmp1 = l1
        tmp2 = l2
        tmp3 = l3
        while tmp1 is not None and tmp2 is not None:
            if tmp1.val < tmp2.val:
                tmp3.val = tmp1.val
                tmp3.next = ListNode(val=None)
                tmp3 = tmp3.next
                tmp1 = tmp1.next
            else:
                tmp3.val = tmp2.val
                tmp3.next = ListNode(val=None)
                tmp3 = tmp3.next
                tmp2 = tmp2.next

        if tmp1 is not None:
            while tmp1 is not None:
                tmp3.val = tmp1.val
                tmp3.next = ListNode(val=None)
                tmp3 = tmp3.next
                tmp1 = tmp1.next
        else:
            while tmp2 is not None:
                tmp3.val = tmp2.val
                tmp3.next = ListNode(val=None)
                tmp3 = tmp3.next
                tmp2 = tmp2.next

        tmp3 = l3
        while tmp3.next.val is not None:
            tmp3 = tmp3.next

        tmp3.next = None
        return l3


a = Solution()
print(a.mergeTwoLists(l1 = [1,2,4], l2 = [1,3,4]))