class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
       
        l = 0
        curr = head
        while curr != None:
            curr = curr.next
            l += 1

        k = (l - n + 1)
        
        
        if k == 1:
            return head.next

        curr = head
        
        for i in range(k - 2):
            curr = curr.next
            
        
        curr.next = curr.next.next

       
        return head
