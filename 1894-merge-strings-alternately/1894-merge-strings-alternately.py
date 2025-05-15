class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        merged = []  # Use a list to build the string efficiently
        counter = 0

        while(len1 > counter or len2 > counter):
            if(len1 > counter):
                merged.append(word1[counter])
            if(len2 > counter):
                merged.append(word2[counter])
            counter += 1

        return "".join(merged)

