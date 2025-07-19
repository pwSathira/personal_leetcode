class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s) # Creates a counter for each occurence of char in string
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap) # this will run in O(n) time

        prev = None
        result = ""

        while maxHeap or prev:
            if prev and not maxHeap:
                return ""

            cnt, char = heapq.heappop(maxHeap)
            result += char
            cnt += 1
            
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            if cnt != 0:
                prev = [cnt, char]

        return result