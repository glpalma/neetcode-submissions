# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        q = [root]

        while q: # a cada andar
            res.append([])
            aux = []
            while q:
                node = q.pop(0)
                aux.append(node)
                res[-1].append(node.val)
            
            for node in aux:
                for side in [node.left, node.right]:
                    if side:
                        q.append(side)

        return res
