class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # target = candies[0]
        result = []
        # for i in candies: 
        #     if target <= i:
        #         target = i
        
        target = max(candies)

        for j in candies:
            if j+extraCandies >= target:
                result.append(True)
            else: 
                result.append(False)

        return result