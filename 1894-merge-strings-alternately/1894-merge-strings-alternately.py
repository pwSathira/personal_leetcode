class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        merged_chars = []  # Use a list to build the string efficiently
        i, j = 0, 0

        # Loop while there are characters in both strings
        while i < len1 and j < len2:
            merged_chars.append(word1[i])
            merged_chars.append(word2[j])
            i += 1
            j += 1

        # If word1 has remaining characters, append them
        while i < len1:
            merged_chars.append(word1[i])
            i += 1

        # If word2 has remaining characters, append them
        while j < len2:
            merged_chars.append(word2[j])
            j += 1

        return "".join(merged_chars)

