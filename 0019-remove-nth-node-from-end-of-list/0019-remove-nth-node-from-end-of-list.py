class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        # Move fast n steps ahead
        for _ in range(n):
            fast = fast.next

        # Move both pointers
        while fast.next:
            slow = slow.next
            fast = fast.next

        # Remove the node
        slow.next = slow.next.next

        return dummy.next