"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #Edge Case
        if not head: 
            return None

        # Pass 1 Create all clones of all new nodes without random pointers
        old_to_new = {}
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val) 
            curr = curr.next # This progresses the while loop to the next node

        # Pass 2 We now link the clones to the random pointers since they exist now
        curr = head # Reset curr to original head? Why is this needed
        while curr:
            clone = old_to_new[curr] # Why do we need clone here?
            clone.next   = old_to_new.get(curr.next) 
            clone.random = old_to_new.get(curr.random) 
            curr = curr.next

        # 4) Return the cloned head
        return old_to_new[head]

