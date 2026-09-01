class Solution:
    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head

        dummy = ListNode(-1)
        dummy.next = head

        prev = dummy
        cur = head

        while cur is not None and cur.next is not None:

            if cur.val == cur.next.val:

                # Skip all duplicate nodes
                while cur.next is not None and cur.val == cur.next.val:
                    cur = cur.next

                prev.next = cur.next

            else:
                prev = prev.next

            cur = cur.next

        return dummy.next