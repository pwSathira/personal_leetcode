class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rad = []
        dir = []

        for i, s in enumerate(senate):
            if s == 'R':
                rad.append(i)
            else:
                dir.append(i)
            
        n = len(senate)

        while rad and dir:
            rad_front = rad.pop(0)
            dir_front = dir.pop(0)

            if rad_front < dir_front:
                rad.append(n)
            else:
                dir.append(n)
            n += 1
        
        return 'Radiant' if rad else 'Dire'