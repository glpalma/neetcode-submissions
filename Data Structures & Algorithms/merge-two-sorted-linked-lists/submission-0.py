class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
            
        curr1 = list1
        curr2 = list2
        new = None
        curr = None

        while curr1 and curr2:
            if curr1.val < curr2.val:
                chosen = curr1
                curr1 = curr1.next
            else:
                chosen = curr2
                curr2 = curr2.next
            
            if not new:
                new = chosen
                curr = chosen
            else:
                curr.next = chosen
                curr = curr.next

        if curr1:
            curr.next = curr1
        if curr2:
            curr.next = curr2

        return new
