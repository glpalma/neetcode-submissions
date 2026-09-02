# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        
        i = 0
        pos = dict()
        curr = head

        while curr:
            if pos.get(curr) != None: # cycle detected
                return True

            pos[curr] = i
            i += 1
            curr = curr.next
        
        return False

        