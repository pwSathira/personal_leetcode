# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base Case
        if not head or not head.next:
            return head

        tempOdd = head # Stores odd nodes tail
        tempEven = head.next # Stores even nodes tail
        evenHead = tempEven # Stores even nodes head

        while tempEven and tempEven.next:
            tempOdd.next = tempEven.next
            tempOdd = tempOdd.next

            tempEven.next = tempOdd.next
            tempEven = tempEven.next
        
        tempOdd.next = evenHead
        return head