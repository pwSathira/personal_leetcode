class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        charIndexA = {}
        charIndexB = {}

        for i in range(len(s)):
            if s[i] not in charIndexA:
                charIndexA[s[i]] = i
            
            if t[i] not in charIndexB:
                charIndexB[t[i]] = i
            
            if charIndexA[s[i]] != charIndexB[t[i]]:
                return False

        return True