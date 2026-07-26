# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num_str = ""
        while l1:
            num_str = str(l1.val) + num_str
            l1 = l1.next

        num_str2 = ""
        while l2:
            num_str2 = str(l2.val) + num_str2
            l2 = l2.next

        total = int(num_str or '0') + int(num_str2 or '0')
        sum_str = str(total)[::-1]

        dummy = ListNode(0)
        curr = dummy
        for digit in sum_str:
            curr.next = ListNode(int(digit))
            curr = curr.next

        return dummy.next
