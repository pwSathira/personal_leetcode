class Solution:
    def reverseWords(self, s: str) -> str:
        output = s.split()
        output.reverse()

        return " ".join(output)