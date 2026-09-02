class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # if s2 contains an anagram of s1
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False

        l = 0
        r = l + n1 - 1

        count1 = {char: s1.count(char) for char in set(s1)}
        countCurr = {char: s2[l : r+1].count(char) for char in set(s2[l : r+1])}

        while r < n2:
            if countCurr == count1:
                return True
            
            r += 1
            if r < n2:
                countCurr[s2[r]] = 1 + countCurr.get(s2[r], 0)

            countCurr[s2[l]] = countCurr.get(s2[l], 0) - 1
            if countCurr[s2[l]] == 0:
                del countCurr[s2[l]]
            l += 1


        return False