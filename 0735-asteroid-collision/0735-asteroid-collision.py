class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        for i in asteroids:
            while result and result[-1] > 0 and i < 0:
                if result[-1] + i < 0: 
                    result.pop()
                elif result[-1] + i:
                    break
                else:
                    result.pop()
                    break
            else: 
                result.append(i)
        
        return result