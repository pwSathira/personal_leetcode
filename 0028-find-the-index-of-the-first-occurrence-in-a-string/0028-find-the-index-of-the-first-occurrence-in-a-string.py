class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        pointer = 0 

        for i in range(len(haystack)+1):
            if haystack[i:i + len(needle)] == needle:
                return i
            
        else:
            return -1
