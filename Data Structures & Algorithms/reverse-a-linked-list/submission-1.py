# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseListWithArray(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        lista = []
        curr = head
        while curr:
            lista.append(curr)
            curr = curr.next

        lista[0].next = None
        for i in range(1, len(lista)):
            node = lista[i]
            node.next = lista[i-1]

        return lista[-1]

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        last = None
        curr = head

        while curr:
            aux = curr.next
            curr.next = last
            last = curr
            curr = aux
        
        return last
