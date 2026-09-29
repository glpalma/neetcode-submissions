# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def rec(l1: Optional[ListNode], l2: Optional[ListNode], add: int = 0) -> Optional[ListNode]:
            if not l1 and not l2: # both lists ended
                if add > 0:
                    return ListNode(val=add)

                return None
            
            if not l1: # only l1 ended, then continue on l2
                assert l2 is not None
                new = ListNode(val = (l2.val + add) % 10)
                new.next = rec(l1, l2.next, (l2.val + add) // 10)
            elif not l2:
                assert l1 is not None
                new = ListNode(val = (l1.val + add) % 10)
                new.next = rec(l1.next, l2, (l1.val + add) // 10)
            else:
                new = ListNode(val = (l1.val + l2.val + add) % 10)
                new.next = rec(l1.next, l2.next, (l1.val + l2.val + add) // 10)

            return new

        return rec(l1, l2)

