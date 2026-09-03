# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next

        pos = count - n
        if pos == 0:
            return head.next
        else:
            i = 0
            curr = head
            while i < pos-1:
                i += 1
                curr = curr.next
            
            curr.next = curr.next.next
        
        return head

    





        
        