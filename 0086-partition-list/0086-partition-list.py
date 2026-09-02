class Solution:
    def partition(self, head, x):
        small = ListNode(0)
        large = ListNode(0)

        small_curr = small
        large_curr = large

        while head:
            if head.val < x:
                small_curr.next = head
                small_curr = small_curr.next
            else:
                large_curr.next = head
                large_curr = large_curr.next

            head = head.next

        # Connect both lists
        large_curr.next = None
        small_curr.next = large.next

        return small.next