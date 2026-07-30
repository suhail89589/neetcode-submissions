# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node = []
        curr = head
        while curr:
            node.append(curr.val)
            curr = curr.next

        for i in range(0, len(node), k):
            if i + k <= len(node):
                node[i:i+k]= node[i:i+k][::-1]

        dummy = ListNode(0)
        curr = dummy
        for val in node:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next

        