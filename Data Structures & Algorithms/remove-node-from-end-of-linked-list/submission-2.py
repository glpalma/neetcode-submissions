# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # solução com duas passadas
    # def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    #     count = 0
    #     curr = head
    #     while curr:
    #         count += 1
    #         curr = curr.next

    #     pos = count - n
    #     if pos == 0:
    #         return head.next
    #     else:
    #         i = 0
    #         curr = head
    #         while i < pos-1:
    #             i += 1
    #             curr = curr.next
            
    #         curr.next = curr.next.next
        
    #     return head

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        first = head
        while i < n:
            i += 1
            first = first.next

        dummy = ListNode(67, head)
        sec = dummy
        while first:
            first = first.next
            sec = sec.next

        sec.next = sec.next.next

        return dummy.next
        


        



    





        
        