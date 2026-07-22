class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = s.replace(" ", "").lower()
        alphaOnly = list(filter(lambda s: s.isalnum(), clean))

        return alphaOnly == alphaOnly[::-1]

        