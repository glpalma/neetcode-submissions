class Solution:
    def isValid(self, s: str) -> bool:
        q = []
        pairs = {')': '(', '}': '{', ']':'['}

        for c in s:
            if c in pairs.values():
                q.append(c)
            elif c in pairs.keys():
                if len(q) > 0 and pairs.get(c) == q[-1]:
                    q.pop()
                else:
                    return False

        return len(q) == 0
