# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: if the list is empty, return None
        if not head:
            return None
        
        stack = []
        curr = head
        
        # 1. Push all nodes onto the stack
        while curr:
            stack.append(curr)
            curr = curr.next
            
        # 2. Pop the first node to be our new head
        new_head = stack.pop()
        curr = new_head
        
        # 3. Pop the rest and link them together
        while stack:
            curr.next = stack.pop()
            curr = curr.next
            
        # 4. Set the final node's next to None to break the old chain
        curr.next = None 
        
        return new_head