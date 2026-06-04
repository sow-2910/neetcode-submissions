# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1,cur2 = l1,l2
        i,j = 1,1
        firstNum, secondNum = 0,0
        while cur1:
            firstNum += cur1.val * i
            cur1 = cur1.next
            i*=10
            

        while cur2:
            secondNum+= cur2.val * j
            cur2 = cur2.next
            j *= 10
        
        total = firstNum + secondNum

        dummy = ListNode(0)
        current = dummy

        if total == 0:
            return ListNode(0)


        while total > 0:
            digit = total % 10
            current.next = ListNode(digit)
            current = current.next
            total //= 10

        return dummy.next 
            

        
    

