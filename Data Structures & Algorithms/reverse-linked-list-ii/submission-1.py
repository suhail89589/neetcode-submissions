class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        node = []
        curr = head
        while curr:
            node.append(curr)
            curr = curr.next
        
       
        left_idx = left - 1
        right_idx = right - 1

        def reverse_segment(node, left, right):
            while left < right:
                node[left], node[right] = node[right], node[left]
                left += 1
                right -= 1
        
        def list_to_linked_list(node):
            if not node:
                return None
            
           
            for i in range(len(node) - 1):
                node[i].next = node[i + 1]
            
            
            node[-1].next = None
            return node[0]

        
        reverse_segment(node, left_idx, right_idx)
        return list_to_linked_list(node)
