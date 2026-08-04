class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxL = 0

        window=set()

        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            maxL = max(maxL, r-l+1)
            window.add(s[r])
        
        return maxL


        