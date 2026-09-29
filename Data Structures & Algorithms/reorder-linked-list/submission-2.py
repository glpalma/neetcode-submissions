# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l = []
        curr = head
        while curr:
            l.append(curr)
            curr = curr.next

        n = len(l)
        prev = l[0]
        for i in range(1, n // 2 + 1):
            prev.next = l[n-i]
            l[n-i].next = l[i]
            prev = l[i]
        
        prev.next = None



        