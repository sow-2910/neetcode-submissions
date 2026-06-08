from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Handle base cases
        if not head or k == 1:
            return head
        
        # Step 1: Initialize dummy node to handle head changes smoothly
        dummy = ListNode(0)
        dummy.next = head
        before_group = dummy
        
        while True:
            # The group starts right after before_group
            group_start = before_group.next
            
            # Step 2: Find the k-th node using your helper function
            group_end = self.getKth(group_start, k)
            
            # If group_end is None, there aren't enough nodes left to reverse
            if not group_end:
                break
                
            # Step 3: Save the node right after this group and break the link
            after_group = group_end.next
            group_end.next = None  
            
            # Step 4: Reverse the isolated group and reconnect it
            before_group.next = self.reverse_list(group_start)
            group_start.next = after_group
            
            # Step 5: Move before_group forward to prepare for the next iteration
            before_group = group_start
            
        return dummy.next

    # Helper Function 1: Find the k-th node from the current node
    def getKth(self, curr: Optional[ListNode], k: int) -> Optional[ListNode]:
        while curr and k > 1:
            curr = curr.next
            k -= 1
        return curr

    # Helper Function 2: Traditional Reverse Linked List
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        return prev