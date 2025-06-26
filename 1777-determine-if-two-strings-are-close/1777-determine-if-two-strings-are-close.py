class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        str1count, str2count = Counter(word1), Counter(word2)
        return str1count.keys() == str2count.keys() and sorted(str1count.values()) == sorted(str2count.values())