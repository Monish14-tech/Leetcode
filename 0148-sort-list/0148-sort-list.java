class Solution {

    public ListNode sortList(ListNode head) {

        if (head == null || head.next == null) {
            return head;
        }

        ListNode mid = getMiddle(head);

        ListNode right = mid.next;

        mid.next = null;

        ListNode leftSorted = sortList(head);

        ListNode rightSorted = sortList(right);

        return merge(leftSorted, rightSorted);
    }

    private ListNode getMiddle(ListNode head) {

        ListNode slow = head;

        ListNode fast = head.next;

        while (fast != null &&
               fast.next != null) {

            slow = slow.next;

            fast = fast.next.next;
        }

        return slow;
    }

    private ListNode merge(
            ListNode a,
            ListNode b
    ) {

        ListNode dummy = new ListNode(0);

        ListNode current = dummy;

        while (a != null && b != null) {

            if (a.val < b.val) {

                current.next = a;

                a = a.next;

            } else {

                current.next = b;

                b = b.next;
            }

            current = current.next;
        }

        if (a != null)
            current.next = a;

        if (b != null)
            current.next = b;

        return dummy.next;
    }
}