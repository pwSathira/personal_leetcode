class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
       freq = {}
       for i in arr:
        freq[i] = freq.get(i, 0) + 1
        
       return len(freq) == len(set(freq.values()))