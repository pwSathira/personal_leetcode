class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left = 0
        if len(s) == 0:
            return True
        for right in range(len(t)):
            if s[left] == t[right]:
                left += 1
            if left >= len(s):
                return True

        return False