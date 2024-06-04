/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        // Dummy Node to act as the starting point of the result list
        ListNode dummy = new ListNode();
        // Pointer node to track the end of the result list
        ListNode resultPointer = dummy;
        // Variables to store the sum of the current digits and the carry value
        int total = 0;
        int carry = 0;
        // Loop until both l1 and l2 are null and carry is zero
        while (l1 != null || l2 != null || carry != 0) {
            // Start with the carry value from the previous addition
            total = carry;
            // If l1 is not null, add its value to total and move to the next node in l1
            if (l1 != null) { 
                total += l1.val;
                l1 = l1.next;
            }
            // If l2 is not null, add its value to total and move to the next node in l2
            if (l2 != null) { 
                total += l2.val;
                l2 = l2.next;
            }
            // Calculate the digit to store in the current node of the result list
            int num = total % 10;
            // Calculate the carry value for the next iteration
            carry = total / 10;
            // Create a new node with the calculated digit and attach it to the result list
            resultPointer.next = new ListNode(num);
            // Move the result pointer to the new node
            resultPointer = resultPointer.next;
        }
        // Return the head of the result list (skipping the dummy node)
        return dummy.next;        
    }
}
