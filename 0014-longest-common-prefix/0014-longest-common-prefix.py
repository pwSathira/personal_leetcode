class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        longest_string = max(strs, key=len, default="")

        for i in range(len(longest_string)):
            for s in strs:
                if len(s) == 0:
                    return ""
                if i >= len(s):
                    return prefix
                elif longest_string[i] != s[i]:
                    return prefix
                
            prefix += longest_string[i]
            print(prefix)
       
        return prefix