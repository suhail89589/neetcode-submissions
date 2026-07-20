class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1. Count the length
        l = 0
        curr = head
        while curr != None:
            curr = curr.next
            l += 1

        k = (l - n + 1)
        
        # FIX FOR FLAW 2: Handle removing the head node explicitly
        if k == 1:
            return head.next

        curr = head
        # FIX FOR FLAW 1: Change range to k-2 to stop right BEFORE the target node
        for i in range(k - 2):
            curr = curr.next
            
        # FIX FOR FLAW 1: Move this OUTSIDE the loop so it only deletes once
        curr.next = curr.next.next

        # FIX FOR FLAW 3: Return the modified list
        return head
