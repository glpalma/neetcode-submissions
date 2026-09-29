# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # O(n) time and O(n) space
    def reorderListIterative(self, head: Optional[ListNode]) -> None:
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
    
    # O(n) time and O(1) space
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2


