class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans: int = 0
        currCount: int = 0
        vowels: str = "aeiou"

        for i in range(len(s)):
            if i >= k and s[i - k] in vowels: 
                currCount -= 1
            currCount += s[i] in vowels
            ans = max(currCount, ans)

        return ans