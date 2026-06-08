# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        
        
        dummy = ListNode(0,head)
        before_group = dummy

        while True:
            group_end = self.getKth(before_group, k)

            if not group_end:
                break
            
            group_start = before_group.next
            after_group = group_end.next
            group_end.next = None

            before_group.next = self.reverse_list(group_start)
            group_start.next = after_group

            before_group = group_start

        return dummy.next

        

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
