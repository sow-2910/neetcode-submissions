# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        stack = []
        curr = head

        while curr:
            stack.append(curr)
            curr = curr.next

        new_head = stack.pop()
        curr = new_head

        while stack:
            curr.next = stack.pop()
            curr = curr.next
        curr.next = None
        return new_head
            





